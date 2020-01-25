from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, reverse
from django.views.generic.edit import UpdateView

from website.userprofile.forms import EditProfileForm
from website.userprofile.models import Profile


class EditProfile(LoginRequiredMixin, UpdateView):
    """Allows an authenticated user to submit a new article."""

    form_class = EditProfileForm
    model = Profile
    template_name = 'userprofile/edit_profile.html'
    context_object_name = "profile"

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
        return reverse("home:index")
