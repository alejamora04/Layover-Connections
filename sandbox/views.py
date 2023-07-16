from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Event
from .forms import EventCreationForm

#import datetime
#from . import events
# Make Datetime objects aware
from django.utils.timezone import datetime
from django.utils import timezone



# Formatting for the splash page portal. 
#TODO Setup the splash page with a demo button to - return render(request, 'layoverconnections/index.html')
def index(request):
	return render(request, 'sandbox/sandbox_placeholder.html')

# Base Event Page to encapsulate all event controls.
def event_base(request):
	return render(request, 'sandbox/event.html')

# Load form variables for the event creation portal. 
def create_event(request):
	if request.method == 'POST':
		Event_Form = EventCreationForm(request.POST)
		if Event_Form.is_valid():
			Event_Form.save()
			messages.success(request, f"Event has been created")
			# TODO Create redirect to updated event
			return render(request, 'sandbox/existing_event.html')
	else:
		Event_Form = EventCreationForm()

	# TODO Read about the role of context with views and rendering forms.
	context = {
		'Event_Form': Event_Form
	}

	return render(request, 'sandbox/create_event.html', context)

# Base Event Page to encapsulate all event controls.
def view_events(request):
	event_list = Event.objects.all()

	start = Event._meta.get_field("start_time")

	# V django.utils.timezone
	time_now = datetime.now()

	start_field_name = 'start_time'
	start_obj = Event.objects.first()
	start = getattr(start_obj, start_field_name)

	field_name = 'end_time'
	obj = Event.objects.first()
	end = getattr(obj, field_name)

	# TypeError: Can't compare offset-naive and offset-aware datetimes

	"""
	Variable	Value
	end_time	
	datetime.datetime(2006, 10, 25, 16, 30, 59, tzinfo=datetime.timezone.utc)
	now	
	datetime.datetime(2023, 7, 16, 16, 25, 55, 457113)
	start_time	
	datetime.datetime(2006, 10, 25, 14, 30, 59, tzinfo=datetime.timezone.utc)
	"""
	# Compares start, end, and current time to determine status.
	# Datetime Comparisons are made in UTC Timezones.
	def event_status(start_time, end_time):
		now = timezone.now()

		if start_time < now and now < end_time:
			status = 'Active'
			return status
		elif now < start_time and now < end_time:
			status = 'Upcoming'
			return status
		elif now > start_time and now > end_time:
			status = 'Finished'
			return status
		return
	
	status = event_status(start, end)	



	context = {
		"Events": event_list,
		"Datetime_now": time_now,
		"Status_Start": start,
		"Status_End": end,
		"Event_Status": status,
	}

	return render(request, 'sandbox/existing_event.html', context)


# [END GOAL] Front-End: Formatted Front-End UI heavy event creation
def end_product(request):
	return render(request, 'sandbox/event_frontend.html')


