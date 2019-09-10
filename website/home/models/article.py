"""Django database models for news articles."""
import re

from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    """Main article model for news articles appearing on the front page."""

    # Content-related fields
    title = models.CharField(
        verbose_name="Titel",
        max_length=256,
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
    content = models.TextField(
        verbose_name="Inhoud",
    )

    # Date-related field
    creation_date = models.DateTimeField(
        verbose_name="Creation date",
        auto_now_add=True,
    )
    pubdate = models.DateTimeField(
        verbose_name="Publication date",
        null=True,
    )
    last_edit = models.DateTimeField(
        verbose_name="Last edited",
        auto_now=True,
    )

    # Status-related fields
    is_published = models.BooleanField(
        verbose_name="Has this article been published?",
        default=False,
    )

    def __str__(self):
        """Returns a string representation of the article."""
        if len(self.title) > 50:
            return f"{self.author} - {self.title[:47]} ({self.publication_status})"
        else:
            return f"{self.author} - {self.title} ({self.publication_status})"

    @property
    def publication_status(self):
        """Returns the publication status as a string."""
        if self.is_published:
            return "published"
        else:
            return "draft"

    @property
    def slug(self) -> str:
        """Returns the url of the article for linking purposes."""
        title = self.title.lower().strip().replace(" ", "-")
        slug = "".join(re.findall(r"[\w-]", title))
        return slug
