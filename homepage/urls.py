from django.urls import path
from homepage import views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("homepage/login.html", views.login, name="login"),
    path("homepage/<str:name>", views.user_profile, name="profile"),
]