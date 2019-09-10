"""Forms related to articles."""
from django.forms import ModelForm

from website.home.models import Article


class NewArticleForm(ModelForm):
    """Form to create a new article."""

    class Meta:
        """Meta-information for the ModelForm."""
        model = Article
        fields = ["title", "content"]
