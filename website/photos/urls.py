from django.urls import path

from .views import ArticleAddPhotos, ArticleRemovePhotos

app_name = "photos"
urlpatterns = [
    path('artikel/<int:pk>/toevoegen', ArticleAddPhotos.as_view(), name='article-add'),
    path('artikel/<int:pk>/verwijderen', ArticleRemovePhotos.as_view(), name="article-remove"),
]
