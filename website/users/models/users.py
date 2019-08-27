"""Represents the default user model for the Minigigs website."""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """The base user model."""

    def __str__(self) -> str:
        """Returns a capitalized version of the user's first name."""
        return self.first_name.capitalize()
