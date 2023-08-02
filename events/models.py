from django.db import models
from django.conf import settings
from django.contrib import auth


from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

"""
MVP Checklist
- Configure Middlewar to assign local CST to views attribute to make status accurate
- Configure special permissions for Host controls over event
- Assign Guest controls based on request to join event. 

MVP Attributes
 Host approval controls,
 Event Guest controls, 
 Thumbnail,

Post MVP Attributes 
 Duration
 Basic Category tags and pagination controls. 

"""

# Prototype model for Events
class Event(models.Model):
    host = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    description = models.CharField(max_length=250,
                    blank=True)
    title = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


    def __str__(self):
        return f"{self.title}"