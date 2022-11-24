from django.urls import path
from layoverconnections import views
from . import views

app_name = "layoverconnections"

urlpatterns = [
    path("", views.index, name="index"),
    path("layoverconnections/login.html", views.login, name="login"),
    path("layoverconnections/<str:name>", views.user_profile, name="profile"),
]