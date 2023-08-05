from django.urls import path
from django.contrib import admin
from . import views

# Pre-Deployment Media Storage recommendations
from django.conf import settings
from django.conf.urls.static import static

# Event paths: events/<view_of_interest>
app_name = "events"
urlpatterns = [
    path("", views.event_base, name="event_base"),
    path("create_event", views.create_event, name="create_event"),
    path("view_events", views.view_events, name="view_events"),
    path("end_product", views.end_product, name="formatted_event"),

    #path("event_details", views.view_my_event, name="event_details"),
    path("<int:event_id>/event_details/", views.event_details, name="event_details"),
] 

# Pre-Deployment check to see if currently in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)