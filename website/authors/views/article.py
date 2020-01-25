"""View that allows an authenticated user to create a new article."""
import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from website.authors.forms.article import NewArticleForm, UpdateArticleForm
from website.home.models import Article

log = logging.getLogger(__name__)


class CreateArticle(LoginRequiredMixin, CreateView):
    """Allows an authenticated user to submit a new article."""

    form_class = NewArticleForm
    model = Article
    template_name = 'authors/create_article.html'

    def get_form(self, form_class=None):
        """Add the appropriate class attributes to the widgets."""
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({"class": "input is-full-width"})
        form.fields['content'].widget.attrs.update({"class": "textarea is-full-width"})
        form.fields['cover_image'].widget.attrs.update({"class": "is-full-width"})
        return form

    def form_valid(self, form):
        """Sets the user as the author."""
        form.instance.author = self.request.user
        form.is_valid()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """Handle post request including files."""
        form = self.form_class(request.POST, request.FILES)
        if self.form_valid(form):
            form.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        """Gets the success url."""
        return reverse("home:article", kwargs={"pk": self.object.pk, "slug": self.object.slug})


class UpdateArticle(LoginRequiredMixin, UpdateView):
    """Allows an authenticated user to submit a new article."""

    form_class = UpdateArticleForm
    model = Article
    template_name = 'authors/update_article.html'
    context_object_name = "article"

    def get_form(self, form_class=None):
        """Add the appropriate class attributes to the widgets."""
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({"class": "input is-full-width"})
        form.fields['content'].widget.attrs.update({"class": "textarea is-full-width"})
        form.fields['cover_image'].widget.attrs.update({"class": "is-full-width"})
        return form

    def form_valid(self, form):
        """Sets the user as the author."""
        form.is_valid()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """Handle post request including files."""
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())
        if self.form_valid(form):
            form.save()
            return redirect(self.get_success_url())
        else:
            return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        """Gets the success url."""
        return reverse("home:article", kwargs={"pk": self.object.pk, "slug": self.object.slug})


class DeleteArticle(LoginRequiredMixin, DeleteView):
    """View to delete the article."""

    model = Article
    success_url = reverse_lazy("home:index")
    template_name = 'authors/delete_article.html'
    context_object_name = "article"
