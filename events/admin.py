from django.contrib import admin
from .models import Event

# Registerred Event property to permit admin views and controls.
admin.site.register(Event)