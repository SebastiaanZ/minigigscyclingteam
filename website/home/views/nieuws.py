"""View for a single article."""
from django.views.generic import DetailView

from ..models import Article


class News(DetailView):
    """Detail view for a single news article."""

    model = Article
    template_name = "home/article.html"
    context_object_name = "article"
