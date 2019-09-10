"""URL routing for the authors app."""
from django.urls import path

from .views import CreateArticle

app_name = "authors"
urlpatterns = [
    path('new/', CreateArticle.as_view(), name="article-new")
]
