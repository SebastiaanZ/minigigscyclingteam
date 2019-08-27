"""Views for landing page."""
from django.http import HttpResponse


def index(request):
    """Index dummy view."""
    return HttpResponse("Hello, world.")
