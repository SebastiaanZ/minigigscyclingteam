from .models import Profile


def create_user_profile(sender, instance, created, **kwargs):
    """Create user profile for newly created users."""
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    """Save user profile when updating user."""
    instance.profile.save()
