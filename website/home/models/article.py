"""Django database models for news articles."""
import hashlib
import pathlib
import re

from django.contrib.auth import get_user_model
from django.db import models


def cover_image_filename(instance: 'Article', filename: str) -> pathlib.Path:
    """Get a filename for the cover image."""
    image = instance.cover_image.open("rb")

    base = hashlib.md5(image.read()).hexdigest()
    extension = pathlib.Path(filename).suffix

    return pathlib.Path("covers") / f"{base}{extension}"


class Article(models.Model):
    """Main article model for news articles appearing on the front page."""

    # Content-related fields
    title = models.CharField(
        verbose_name="Titel",
        max_length=256,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    content = models.TextField(
        verbose_name="Inhoud",
    )

    # Date-related field
    creation_date = models.DateTimeField(
        verbose_name="Creation date",
        auto_now_add=True,
    )
    pubdate = models.DateTimeField(
        verbose_name="Publication date",
        auto_now_add=True,
        null=True,
    )
    last_edit = models.DateTimeField(
        verbose_name="Last edited",
        auto_now=True,
    )

    # Status-related fields
    is_published = models.BooleanField(
        verbose_name="Has this article been published?",
        default=True,
    )

    # Add cover image field
    cover_image = models.ImageField(
        verbose_name="Artikelfoto",
        upload_to=cover_image_filename,
        default="/static/images/photos/default_image.jpeg",
    )

    def __str__(self):
        """Returns a string representation of the article."""
        if len(self.title) > 50:
            return f"{self.author} - {self.title[:47]} ({self.publication_status})"
        else:
            return f"{self.author} - {self.title} ({self.publication_status})"

    @property
    def image_url(self):
        """Get the image cover if it exists, otherwise return the default image."""
        if self.cover_image:
            return self.cover_image.url

        return "/static/images/photos/default_image.jpeg"

    @property
    def publication_status(self):
        """Returns the publication status as a string."""
        if self.is_published:
            return "published"
        else:
            return "draft"

    @property
    def slug(self) -> str:
        """Returns the url of the article for linking purposes."""
        title = self.title.lower().strip().replace(" ", "-")
        slug = "".join(re.findall(r"[\w-]", title))
        return slug

    class Meta:
        """Meta options for this model."""

        ordering = ['-pubdate']
