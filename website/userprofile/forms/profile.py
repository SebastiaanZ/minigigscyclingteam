"""Forms related to articles."""
import django.forms

from website.userprofile.models import Profile
from website.utils.widgets import ClearableImageInput


class EditProfileForm(django.forms.ModelForm):
    """Form to change your profile picture."""

    profile_picture = django.forms.ImageField(required=False, widget=ClearableImageInput,
                                              label="Profielfoto")

    class Meta:
        """Meta-information for the ModelForm."""

        model = Profile
        fields = ["profile_picture"]
