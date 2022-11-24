from django.urls import path
from layoverconnections import views
from . import views

app_name = "layoverconnections"

# homepage is django placeholder consider removing it
urlpatterns = [
    path("", views.index, name="index"),
    path("layoverconnections/register", views.register_request, name="register"),
    path("layoverconnections/login.html", views.login, name="login"),
    path("layoverconnections/<str:name>", views.user_profile, name="profile"),
]