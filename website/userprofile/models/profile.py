from django.contrib.auth import get_user_model
from django.db import models

from website.utils import ResizedHashNameImageField


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

    profile_picture = ResizedHashNameImageField(
        verbose_name="Profielfoto",
        upload_to="avatars",
        null=True,
        blank=True,
    )

    @property
    def avatar_url(self) -> str:
        """Get the avatar for this user."""
        if self.profile_picture:
            return self.profile_picture.url

        return "/static/images/default_avatar.jpg"
