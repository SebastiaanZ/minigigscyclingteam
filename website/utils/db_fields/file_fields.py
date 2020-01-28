import hashlib
import io
import sys
from typing import Optional

from PIL import Image, ImageOps
from django.core import checks
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db.models import ImageField


class ResizedHashNameImageField(ImageField):
    """A custom ImageField class that will resize the images and uses the file hash as filename."""

    def __init__(
        self,
        verbose_name: Optional[str] = None,
        name: Optional[str] = None,
        max_width: int = 1620,
        max_height: int = 1620,
        width_field: Optional[str] = None,
        height_field: Optional[str] = None,
        **kwargs
    ) -> None:
        self.max_width = max_width
        self.max_height = max_height

        super().__init__(verbose_name, name, width_field, height_field, **kwargs)

    def pre_save(self, model_instance, add):
        """Prepares the image for saving by scaling it to the desired dimensions."""
        file = getattr(model_instance, self.attname)
        if file and not file._committed:
            # Open the image with Pillow and save the original format attribute
            im = Image.open(file.file)
            im_format = im.format

            # If the image contains exif rotation data, rotate it accordingly
            im = ImageOps.exif_transpose(im)

            # Rescale the image, if necessary
            im.thumbnail((self.max_width, self.max_height), resample=Image.LANCZOS)

            # Save it to an in-memory file
            temp = io.BytesIO()
            im.save(temp, format=im_format, quality=75)

            # Hash the contents for a filename
            filename = f"{hashlib.md5(temp.getvalue()).hexdigest()}.{im_format}"

            # Create a new InMemoryUploadedFile
            new_file = InMemoryUploadedFile(
                temp, self.name, filename, f'image/{im_format.lower()}', sys.getsizeof(temp), None
            )

            # Reassign the `file` and `name` attributes
            file.file = new_file
            file.name = filename

            # Save the file
            file.save(file.name, file.file, save=False)
        return file

    def check(self, **kwargs):
        """Check maximum dimension values for integrity."""
        return [
            *super().check(**kwargs),
            *self._check_maximum_dimension_values(),
        ]

    def _check_maximum_dimension_values(self):
        """Check if the maximum dimension field values were set with an integer."""
        if not isinstance(self.max_width, int) or not isinstance(self.max_height, int):
            return [
                checks.Error(
                    f"{self.__class__.__name__}'s 'max_width' and `max_height` arguments"
                    " must be integers.",
                    obj=self,
                    hint='Provide integer values',
                )
            ]
        else:
            return []
