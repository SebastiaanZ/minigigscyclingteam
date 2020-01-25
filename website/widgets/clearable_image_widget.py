from django.forms import ClearableFileInput


class ClearableImageInput(ClearableFileInput):
    """Clearable Image Input that displays the current image instead of linking it."""

    template_name = "widgets/clearable_image_widget.html"
    input_text = "Selecteer nieuwe foto:"
    clear_checkbox_label = "Verwijder huidige foto:"
