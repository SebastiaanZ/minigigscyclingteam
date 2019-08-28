"""Views for landing page."""
from django.views.generic import ListView

from ..models import Article


class Home(ListView):
    """The homepage view that displays a list of most recent articles."""

    model = Article
    template_name = "home/home.html"
    context_object_name = 'articles'
