from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

"""
MVP Properties
 Creator, 
 Title, x 
 Date, x
 Start time, x
 End Time, x
 Status (Active, upcoming, finished)

Post MVP
 Thumbnail, 
 Guest, 
 Descriptions,
 Host approval controls,
 Duration 


"""

# Prototype model for Events
class Event(models.Model):
    title = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    def __str__(self):
        return f"{self.title}"
