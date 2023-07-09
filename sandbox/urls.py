from django.urls import path
from django.contrib import admin
from . import views

# Pre-Deployment Media Storage recommendations
from django.conf import settings
from django.conf.urls.static import static

app_name = "sandbox"

# Homepage is django placeholder consider removing it
urlpatterns = [
    # Sandbox paths: sandbox/<view_of_interest>
    # placeholder default path sandbox/index
    path("index/", views.index, name="index"),
    # sandbox/<view_of_interest>
    path("events/", views.event_base, name="event_base"),
    path("create_event", views.create_event, name="create_event"),
    path("view_events", views.view_events, name="view_events"),
    path("end_product", views.end_product, name="formatted_event")
] 

# Pre-Deployment check to see if currently in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)