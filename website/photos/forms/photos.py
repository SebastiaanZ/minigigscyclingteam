import logging
from typing import Generator

from django import forms

from website.home.models import Article

log = logging.getLogger(__name__)


class MultiplePhotosForm(forms.Form):
    """A form to upload multiple photos at once."""

    photos = forms.ImageField(
        label="Foto's",
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )


class RemovePhotosFromArticleForm(forms.Form):
    """A form to remove photos from an article."""

    def __init__(self, article: Article, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super().__init__(*args, **kwargs)

        for photo in article.photos.all():
            field = forms.BooleanField(
                label=photo.image.url,
                required=False,
            )
            field.creator = photo.creator
            field.creation_date = photo.creation_date
            field.n_articles = photo.articles.all().distinct().count()
            self.fields[f"photo_{photo.pk}"] = field

    @property
    def photos_to_remove(self) -> Generator[int, None, None]:
        """Yield the photos that we want to remove from the article."""
        for name, checked in self.cleaned_data.items():
            if name.startswith("photo_") and checked:
                _, _, pk = name.partition("_")
                yield int(pk)
