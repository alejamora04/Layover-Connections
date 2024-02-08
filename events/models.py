from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Prototype model for Events
class Event(models.Model):
    description = models.CharField(max_length=250, blank=True)
    title = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    participants = models.ManyToManyField(User)
    # Add a field to store the host's user id.
    host = models.IntegerField(null=True)
    # Add Event Thumbnail and provide a default.
    event_thumbnail = models.ImageField(default='event_placeholder.jpg', upload_to='event_thumbnails')

    # Host permissions created via model attributes.
    class Meta:
        permissions = (('can_edit_event', 'Host Controls'),)

    def __str__(self):
        return f"Title: {self.title} \n"
    
    # Allows for get object or 404 & to insert args into URL route reqs: (/host/title)
    def get_absolute_url(self):
        return reverse('events:event_details', kwargs={"event_id": self.pk})
    
    # Provide Manager for saving event thumbnail (Maybe unneccesary/redundant)
    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)

        img = Image.open(self.event_thumbnail.path)

        # Provide size restrictions of user uploaded images (300x300)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.event_thumbnail.path)