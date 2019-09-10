"""Custom login form that sets the correct widget class attributes."""
from django import forms
from django.contrib.auth.forms import AuthenticationForm as AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class AuthForm(AuthenticationForm):
    """Custom authentication form."""

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'input is-rounded'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input is-rounded'}),
    )
