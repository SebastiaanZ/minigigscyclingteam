"""Models for storing photos."""
from django.contrib.auth import get_user_model
from django.db import models

from website.utils import ResizedHashNameImageField


class Photo(models.Model):
    """Model that represents a single, stored photo"""

    image = ResizedHashNameImageField(
        verbose_name="Foto",
        max_width=900,
        max_height=600,
        upload_to="photos"
    )

    creator = models.ForeignKey(
        get_user_model(),
        verbose_name="Gebruiker",
        on_delete=models.PROTECT,
    )

    creation_date = models.DateTimeField(
        verbose_name="Uploaddatum",
        auto_now_add=True,
    )
