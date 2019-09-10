from django.urls import path, re_path

from .views import LoginPage, LogoutPage

app_name = "users"
urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutPage.as_view(), name='logout'),
]
