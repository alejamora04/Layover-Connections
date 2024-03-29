from django.urls import path
from django.contrib import admin
from layoverconnections import views
from . import views

# Pre-Deployment Media Storage recommendations
from django.conf import settings
from django.conf.urls.static import static

app_name = "layoverconnections"

# Homepage is django placeholder consider removing it
urlpatterns = [
    path("", views.index, name="index"),
    path("main", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("user_profile", views.user_profile, name="profile"),
    path("<int:user_profile_id>/edit_profile", views.edit_profile, name="editprofile"),
    path("<int:user_id>/user_profile/", views.public_profile, name="public_profile"),
    path("delete_profile", views.delete_profile, name="delete_profile"),
    path("about_me", views.edit_bio, name="aboutme"),
    path("events", views.create_event, name="events"),
] 

# Pre-Deployment check to see if currently in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)