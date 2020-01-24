"""URL routing for the authors app."""
from django.urls import path, re_path

from .views import CreateArticle, DeleteArticle, UpdateArticle

app_name = "authors"
urlpatterns = [
    path('nieuw/', CreateArticle.as_view(), name="article-new"),
    re_path(r'bewerk/(?P<pk>[\d]{1,})/$', UpdateArticle.as_view(), name='article-update'),
    re_path(r'verwijder/(?P<pk>[\d]{1,})/$', DeleteArticle.as_view(), name='article-delete'),
]
