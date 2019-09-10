"""Default view for the login page."""
from django.contrib.auth.views import LoginView, LogoutView

from ..forms import AuthForm


class LoginPage(LoginView):
    """The default login view."""

    template_name = "users/login.html"
    form_class = AuthForm


class LogoutPage(LogoutView):
    """The default logout view."""
    form = AuthForm
