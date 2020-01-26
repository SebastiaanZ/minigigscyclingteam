from django.db import models
from django.utils import timezone


class PublicationDateTimeField(models.DateTimeField):
    """A custom DateTimeField that is populated on creation, but can be edited."""

    def pre_save(self, model_instance, add):
        """Only set the current datetime if we are adding a new object to the database."""
        if add:
            setattr(model_instance, self.attname, timezone.now())
        return super().pre_save(model_instance, add)
