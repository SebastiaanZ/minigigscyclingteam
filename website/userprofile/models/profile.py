import hashlib
import pathlib

from django.contrib.auth import get_user_model
from django.db import models


def profile_picture_filename(instance: 'Profile', filename: str) -> pathlib.Path:
    """Get a filename for the cover image."""
    image = instance.profile_picture.open("rb")

    base = hashlib.md5(image.read()).hexdigest()
    extension = pathlib.Path(filename).suffix

    return pathlib.Path("avatars") / f"{base}{extension}"


class Profile(models.Model):
    """An extended user profile for our site's users."""

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE
    )

    is_cyclist = models.BooleanField(
        verbose_name="Is this a member of team?",
        default=False,
    )

    profile_picture = models.ImageField(
        verbose_name="Profielfoto",
        upload_to=profile_picture_filename,
        null=True,
        blank=True,
    )

    @property
    def avatar_url(self) -> str:
        """Get the avatar for this user."""
        if self.profile_picture:
            return self.profile_picture.url

        return "/static/images/default_avatar.jpg"
