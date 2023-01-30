from django.urls import path
from django.contrib import admin
from layoverconnections import views
from . import views

# Pre-Deployment Media Storage recommendations
from django.conf import settings
from django.conf.urls.static import static

app_name = "layoverconnections"

# homepage is django placeholder consider removing it
urlpatterns = [
    path("", views.index, name="index"),
    path("layoverconnections", views.homepage, name="homepage"),
    path("layoverconnections/register", views.register_request, name="register"),
    path("layoverconnections/login.html", views.login_view, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("layoverconnections/user_profile.html", views.user_profile, name="profile"),
    path("layoverconnections/edit_profile.html", views.edit_profile, name="editprofile")
] 

# Pre-Deployment check to see if currently in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)