from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse

from website.users.forms import ChangePasswordForm


class ChangePassword(LoginRequiredMixin, PasswordChangeView):
    """Allow the user to change their password."""

    template_name = "users/change_password.html"
    form_class = ChangePasswordForm

    def get_success_url(self):
        """Get success url with `password changed` message."""
        messages.add_message(
            self.request,
            messages.SUCCESS,
            message="Jouw wachtwoord is gewijzigd.",
            extra_tags='Wachtwoord gewijzigd'
        )
        return reverse("home:index")
