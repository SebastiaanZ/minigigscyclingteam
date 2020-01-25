"""Views module of the users app."""
from .change_password import ChangePassword
from .login import LoginPage, LogoutPage

__all__ = ["LoginPage", "LogoutPage", "ChangePassword"]
