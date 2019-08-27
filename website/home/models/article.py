"""Django database models for news articles."""
from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    """Main article model for news articles appearing on the front page."""

    title = models.CharField(max_length=256)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    content = models.TextField(verbose_name="Main content of the article")
    pubdate = models.DateTimeField(verbose_name="Publication date", auto_now_add=True)
    last_edit = models.DateTimeField(verbose_name="Last edited", auto_now=True)

    def __str__(self):
        """Returns a string representation of the article."""
        if len(self.title) > 50:
            return f"{self.author} - {self.title[:47]} ({self.pubdate})"
        else:
            return f"{self.author} - {self.title} ({self.pubdate})"
