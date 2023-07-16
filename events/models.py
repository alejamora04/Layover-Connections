from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

"""
MVP Checklist
- Assign CST to views attribute to make status accurate
- Link to Host based on User model allow them mod controls over event
- Assign Guest controls based on request to join event. 

MVP Attributes
 Descriptions,
 Host approval controls,
 Event Guest controls, 
 Thumbnail, 

Post MVP Attributes 
 Duration 


"""

# Prototype model for Events
class Event(models.Model):
    title = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    def __str__(self):
        return f"{self.title}"