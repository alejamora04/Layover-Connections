from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

from django.contrib import auth
from django.utils import timezone
from PIL import Image

"""
MVP Checklist
- Configure Middleware to assign local CST to views attribute to make status accurate
Attributes
 Host approval controls[In Progress],
 Thumbnail,
 
Post MVP Attributes 
 Duration
 Basic Category tags and pagination controls. 
"""

# Prototype model for Events
class Event(models.Model):
    description = models.CharField(max_length=250,
                    blank=True)
    title = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(User)

    # Host permissions created via model attributes.
    class Meta:
        permissions = (('can_edit_event', 'Host Controls'),)

    def __str__(self):
        return f"Title: {self.title} \n"
    
    # Allows for get object or 404 & to insert args into URL route reqs: (/host/title)
    def get_absolute_url(self):
        return reverse('events:event_details', kwargs={"event_id": self.pk})