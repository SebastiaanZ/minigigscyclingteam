from django.urls import path, re_path

from .views import Home, News

app_name = "home"
urlpatterns = [
    path('', Home.as_view(), name='index'),
    re_path(r'nieuws/(?P<pk>[\d]{1,})-(?P<slug>[\w-]+[\w]+)/$', News.as_view(), name='article')
]
