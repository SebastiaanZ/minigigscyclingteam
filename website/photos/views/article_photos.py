import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, reverse
from django.views.generic import FormView, UpdateView

from website.home.models import Article
from website.photos.forms import MultiplePhotosForm, RemovePhotosFromArticleForm
from website.photos.models import Photo

log = logging.getLogger(__name__)


class ArticlePhotos(LoginRequiredMixin, FormView):
    """A class to create Article Photo views."""

    def get_context_data(self, **kwargs):
        """Get context data for the view."""
        context = super().get_context_data(**kwargs)

        article_pk = self.kwargs["pk"]
        article = get_object_or_404(Article, pk=article_pk)

        context["article"] = article

        return context

    def get_success_url(self):
        """Redirect the user to the article we've added the photos to."""
        article_pk = self.kwargs["pk"]
        article = get_object_or_404(Article, pk=article_pk)
        return reverse("home:article", kwargs={"pk": article.pk, "slug": article.slug})


class ArticleAddPhotos(ArticlePhotos):
    """A view to add photos to an article."""

    form_class = MultiplePhotosForm
    template_name = "photos/article_add_photos.html"

    def post(self, request, *args, **kwargs):
        """Process the form and handle the image files."""
        form = self.get_form()
        if form.is_valid():
            for file in request.FILES.getlist("photos"):
                photo = Photo(image=file, creator=request.user)
                photo.save()
                photo.articles.add(self.kwargs["pk"])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ArticleRemovePhotos(LoginRequiredMixin, UpdateView):
    """A view that allows a logged-in user to remove photos from an article."""

    model = Article
    form_class = RemovePhotosFromArticleForm
    template_name = "photos/article_remove_photos.html"

    def get_form_kwargs(self):
        """Get the form kwargs for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs["article"] = self.object
        return kwargs

    def form_valid(self, form):
        """Handle a valid form by removing the photos from the article."""
        count = 0
        for photo in form.photos_to_remove:
            self.object.photos.remove(photo)
            count += 1

        verb = "is" if count == 1 else "zijn"
        noun = "foto" if count == 1 else "foto's"

        title = "Foto's verwijderd" if count > 0 else "Geen foto's verwijderd"

        messages.add_message(
            self.request,
            messages.SUCCESS,
            message=f"Er {verb} {count} {noun} verwijderd uit het artikel.",
            extra_tags=title,
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """Redirect the user to the article the photos were removed from."""
        return reverse("home:article", kwargs={
            "pk": self.object.pk, "slug": self.object.slug
        })
