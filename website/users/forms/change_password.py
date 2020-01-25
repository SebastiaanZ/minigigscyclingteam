"""Custom login form that sets the correct widget class attributes."""
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _


class ChangePasswordForm(PasswordChangeForm):
    """Custom authentication form."""

    old_password = forms.CharField(
        label=_("Oud wachtwoord"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input is-rounded'}),
    )

    new_password1 = forms.CharField(
        label=_("Nieuw wachtwoord"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input is-rounded'}),
    )

    new_password2 = forms.CharField(
        label=_("Herhaal nieuw wachtwoord"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'input is-rounded'}),
    )
