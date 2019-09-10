"""View that allows an authenticated user to create a new article."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import reverse
from django.http import Http404

from website.home.models import Article


class CreateArticle(LoginRequiredMixin, CreateView):
    """Allows an authenticated user to submit a new article."""
    model = Article
    fields = ['title', 'content']
    template_name = 'authors/article.html'

    def get_form(self, form_class=None):
        """Add the appropriate class attributes to the widgets."""
        form = super().get_form(form_class)
        form.fields['title'].widget.attrs.update({"class": "input is-full-width"})
        form.fields['content'].widget.attrs.update({"class": "textarea is-full-width"})
        return form

    def form_valid(self, form):
        """Sets the user as the author."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """Gets the success url."""
        return reverse("home:article", kwargs={"pk": self.object.pk, "slug": self.object.slug})
