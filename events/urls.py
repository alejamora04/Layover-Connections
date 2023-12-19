from django.urls import path
from django.contrib import admin
from . import views

# Pre-Deployment Media Storage recommendations
from django.conf import settings
from django.conf.urls.static import static

# Event paths: events/<view_of_interest>
app_name = "events"
urlpatterns = [
    path("", views.view_events, name="view_events"),
    path("create_event", views.create_event, name="create_event"),
    path("end_product", views.end_product, name="formatted_event"),
    path("<int:event_id>/event_details/", views.event_details, name="event_details"),
    path("<int:event_id>/edit_event/", views.edit_event, name="edit_event"),
    path("<int:event_id>/delete_event/", views.delete_event, name="delete_event"),
] 

# Pre-Deployment check to see if currently in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)