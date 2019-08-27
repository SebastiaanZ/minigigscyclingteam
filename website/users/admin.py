"""Configurations for the Django Admin pages for this app."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


admin.site.register(User, UserAdmin)
