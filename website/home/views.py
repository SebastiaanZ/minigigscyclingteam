from django.http import HttpResponse


def index(request):
    """Index dummy view."""
    return HttpResponse("Hello, world. You're at the polls index.")
