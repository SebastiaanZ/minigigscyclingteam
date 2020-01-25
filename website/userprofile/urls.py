"""URL routing for the authors app."""
from django.urls import re_path

from website.userprofile.views import EditProfile

app_name = "userprofile"
urlpatterns = [
    re_path(r'bewerk/(?P<pk>[\d]{1,})/$', EditProfile.as_view(), name='profile-edit'),
]
