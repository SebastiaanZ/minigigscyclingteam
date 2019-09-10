"""Models for storing photos."""
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Photo(models.Model):
    """Model that represents a single, stored photo"""

    filename = models.CharField(
        verbose_name='filename of the photo on disk',
        max_length=64,
        blank=True,
    )
    uploaded = models.DateTimeField(
        verbose_name="Datum waarop de foto is geüpload",
        auto_now_add=True
    )
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    width = models.IntegerField(
        verbose_name="Breedte van de photo",
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(8192)
        ]
    )
    height = models.IntegerField(
        verbose_name="Hoogte van de photo",
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(8192)
        ]
    )
