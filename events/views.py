from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Event
from .forms import EventCreationForm

# Enables Datetime objects to become aware
from django.utils import timezone


# Formatting for the splash page portal. 
#TODO Setup the splash page with a demo button to - return render(request, 'layoverconnections/index.html')
# Base Event Page to encapsulate all event controls.
def event_base(request):
	return render(request, 'events/event_splashpage.html')

# Load form variables for the event creation portal. 
def create_event(request):
	if request.method == 'POST':
		Event_Form = EventCreationForm(request.POST)
		if Event_Form.is_valid():
			Event_Form.save()
			messages.success(request, f"Event has been created")
			# TODO Create redirect to updated event
			return render(request, 'events/existing_event.html')
	else:
		Event_Form = EventCreationForm()

	# TODO Read about the role of context with views and rendering forms.
	context = {
		'Event_Form': Event_Form
	}

	return render(request, 'events/create_event.html', context)

# Base Event Page to encapsulate all event controls.
def view_events(request):
	event_list = Event.objects.all()

	# V django.utils.timezone
	# TODO Set this to CST as a barometer before Introducing comparison logic.
	CST_time_now = timezone.now()

	# Access Model Start & End DateTime Field Values.
	model_start_time = 'start_time'
	model_end_time = 'end_time'
	model_object = Event.objects.first()

	start = getattr(model_object, model_start_time)
	end = getattr(model_object, model_end_time)

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
		"Datetime_now": CST_time_now,
		"Status_Start": start,
		"Status_End": end,
		"Event_Status": status,
	}

	return render(request, 'events/existing_event.html', context)


# [END GOAL] Front-End: Formatted Front-End UI heavy event creation
def end_product(request):
	return render(request, 'events/event_frontend.html')
