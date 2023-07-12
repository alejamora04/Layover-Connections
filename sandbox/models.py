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
        event_properties = (f"Event: {Event.title}\n"+
                    f"Start Time: {Event.start_time}\n"+
                    f"End Time: {Event.end_time}\n")
        return event_properties
    


    
"""
# Model Properties
class Event:
    def __init__(self, name, start, end, status, duration):
        Event.name = str(name)
        Event.start = start
        Event.end = end
        Event.status = status
        Event.duration = duration

    def __str__(self):
        event_properties = (f"Event: {Event.name}\n"+
                            f"Start Time: {Event.start}\n"+
                            f"End Time: {Event.end}\n"+
                            f"Status: {Event.status}\n"+
                            f"Duration: {Event.duration}\n")
        return event_properties

# Inputs (start_time, end_time, current_time)
def event_status(start, end, now):
    if start < now and now < end:
        status = 'Active'
    elif now < start and now < end:
        status = 'Upcoming'
    elif now > start and now > end:
        status = 'Finished'
    return status

    
start_time = datetime.datetime(2023, 8, 24, 9 ,34)
end_time = datetime.datetime(2023, 8, 24, 15 ,34)
event_duration = (end_time - start_time)
time_now = datetime.datetime.now()
current_status = event_status(start_time, end_time, time_now)

house_party = Event("House Party", start_time, end_time, current_status, event_duration)
print(house_party)


"""