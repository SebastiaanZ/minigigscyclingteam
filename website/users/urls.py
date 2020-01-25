from django.urls import path

from .views import ChangePassword, LoginPage, LogoutPage

app_name = "users"
urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutPage.as_view(), name='logout'),
    path('wachtwoord/', ChangePassword.as_view(), name="change-password")
]
