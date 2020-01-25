import logging

from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

log = logging.getLogger(__name__)


class UserprofileConfig(AppConfig):
    """App configuration for the extended user profile."""

    name = 'website.userprofile'

    def ready(self):
        """Add signal handlers for User post_save."""
        from website.userprofile.signals import create_user_profile, save_user_profile

        post_save.connect(create_user_profile, sender=get_user_model())
        post_save.connect(save_user_profile, sender=get_user_model())
