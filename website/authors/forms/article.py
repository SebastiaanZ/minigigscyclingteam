"""Forms related to articles."""
import django.forms

from website.home.models import Article
from website.utils import ClearableImageInput


class NewArticleForm(django.forms.ModelForm):
    """Form to create a new article."""

    cover_image = django.forms.ImageField(
        required=False, widget=ClearableImageInput, label="Artikelfoto"
    )

    class Meta:
        """Meta-information for the ModelForm."""

        model = Article
        fields = ["title", "content", "cover_image"]


class UpdateArticleForm(django.forms.ModelForm):
    """Form to edit an existing article."""

    cover_image = django.forms.ImageField(
        required=False, widget=ClearableImageInput, label="Artikelfoto"
    )

    class Meta:
        """Meta-information about the ModelForm."""

        model = Article
        fields = ["title", "content", "cover_image", "pubdate"]
