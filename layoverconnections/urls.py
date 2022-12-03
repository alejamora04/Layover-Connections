from django.urls import path
from django.contrib import admin
from layoverconnections import views
from . import views

app_name = "layoverconnections"

# homepage is django placeholder consider removing it
urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
    path("layoverconnections/register", views.register_request, name="register"),
    path("layoverconnections/login.html", views.login_view, name="login"),
    path("layoverconnections/<str:name>", views.user_profile, name="profile"),
]