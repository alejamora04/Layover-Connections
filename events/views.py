from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from .models import Event
from .forms import EventCreationForm
# Enables Datetime objects to become aware
from django.utils import timezone


# Base Event Page to encapsulate all event controls.
def event_base(request):
	return render(request, 'events/event_splashpage.html')

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
	# Datetime Comparisons are made in UTC Timezones. Need to add a date comparison as well.
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

# Load form variables for the event creation portal.
@login_required 
def create_event(request):
	if request.method == 'POST':
		Event_Form = EventCreationForm(request.POST)
		# Store host & title to add the current user as the host.
		host = request.user

		if Event_Form.is_valid():
			event_title = Event_Form.cleaned_data['title']
			Event_Form.save()
			# Retrieve event and add current user as host.
			New_Event = Event.objects.get(title=event_title)
			New_Event.participants.add(host)
			New_Event.save()

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


# Render single event details Allow the host to edit and for guest to join.
def event_details(request, event_id):
	event_details = get_object_or_404(Event, pk = event_id)

	# Allow user to join event.
	if request.method == "POST":
		event_details.participants.add(request.user)
		event_details.save()
		messages.success(request, f"You have joined the event.")
		return render(request, 'events/event_details.html', {"event_details": event_details})

	context = {
		"event_details": event_details,
	}

	return render(request, 'events/event_details.html', context)


"""
	event_details = get_object_or_404(Event, pk = event_id)

	context = {
		"event_details": event_details,
	}

	return render(request, 'events/event_details.html', context)
"""


# Allow the host to edit event details on the front end.
def edit_event(request, event_id):
	# Load event model details to prepopulate the form fields.
	event_details = get_object_or_404(Event, pk = event_id)

	if request.method == "POST":
		update_form = EventCreationForm(request.POST, instance=event_details)
		if update_form.is_valid():
			update_form.save()
			messages.success(request, f"Your Event {format(update_form)} has been updated.")
			return render(request, 'events/event_details.html', {"event_details": event_details})
	
	else:
		update_form = EventCreationForm(instance=event_details)

	context = {
		"event_details": event_details,
		"update_form": update_form,
	}
		 

	return render(request, 'events/edit_event.html', context)


# Allow the host to edit event details on the front end.
def delete_event(request, event_id):
	# Load event model details to prepopulate the form fields.
	event_to_delete = get_object_or_404(Event, pk = event_id)
	
	context = {
		"delete_event": event_to_delete,
	}

	if request.method == "POST":
		event_to_delete.delete()

		return render(request, 'events/existing_event.html')
		 
	return render(request, 'events/delete_event.html', context)


# [END GOAL] Front-End: Formatted Front-End UI heavy event creation
def end_product(request):
	return render(request, 'events/event_frontend.html')
