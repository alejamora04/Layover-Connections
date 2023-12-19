from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from events.models import Event, User
from django.contrib import messages
from .forms import EventCreationForm


"""

MVP Checklist
- Configure Middleware to assign local CST to views attribute to make status accurate

"""

# Base Event Page to encapsulate all event controls.
def event_base(request):
	return render(request, 'events/event_splashpage.html')


"""


Prototype: Establish Event status by comparing model object start time, end time, and current time
TODO:
1. Configure Middleware to convert UDT to CST
2. Establish chron job to schedule event status refreshed.

from django.utils import timezone 

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


"""



# Base Event Page to encapsulate all event controls.
def view_events(request):
	event_list = Event.objects.all()

	context = {
		"Events": event_list,
	}

	return render(request, 'events/existing_event.html', context)

# Load form variables for the event creation portal.
@login_required 
def create_event(request):
	if request.method == 'POST':
		Event_Form = EventCreationForm(request.POST, request.FILES)
		# Store host & title, apply host controls to the current user.
		host = request.user

		if Event_Form.is_valid():
			event_title = Event_Form.cleaned_data['title']
			Event_Form.save()
			# Retrieve event and add current user as participant, store user to make them a host with permissions in edit_details().
			New_Event = Event.objects.get(title=event_title)
			New_Event.host = (host.id)
			New_Event.participants.add(host)
			# Provide Host with elevated event permissions to allow them to modify/delete the event.
			edit_permission = Permission.objects.get(codename='can_edit_event')
			print(f"This is the permission object queried {edit_permission}")
			host.user_permissions.add(edit_permission)

			New_Event.save()

			messages.success(request, f"Event has been created")
			return redirect(reverse("events:view_events"))
	else:
		Event_Form = EventCreationForm()

	context = {
		'Event_Form': Event_Form
	}

	return render(request, 'events/create_event.html', context)


# Render single event details Allow the host to edit and for guest to join.
def event_details(request, event_id):
	event_details = get_object_or_404(Event, pk = event_id)
	# Query Host Participant details to link profile and thumbnail.
	host_id = event_details.host
	host = User.objects.get(id=host_id)

	# Allow user to join event.
	if request.method == "POST":
		event_details.participants.add(request.user)
		event_details.save()
		messages.success(request, f"You have joined the event.")
		return render(request, 'events/event_details.html', {"event_details": event_details})

	context = {
		"event_details": event_details,
		"host": host,
	}

	return render(request, 'events/event_details.html', context)


# Allow Host User to modify the event. Raise HTTP 403 Error code if the user is unauthorized.
@permission_required('events.can_edit_event', raise_exception=True)
def edit_event(request, event_id):
	# Load event model details to prepopulate the form fields.
	event_details = get_object_or_404(Event, pk = event_id)
	update_form = EventCreationForm(instance=event_details)

	# Store user id to validate against event host id
	current_user = request.user
	host = current_user.id
	event_host = event_details.host

	# Only allow user to modify event details if they're a host.
	if host == event_host:
		if request.method == "POST":
			update_form = EventCreationForm(request.POST,
								   		 	request.FILES,
											instance=event_details)
			if update_form.is_valid():
				update_form.save()
				# FIXME Django routing messages to admin/ login portal url insert messages with JavaScript
				messages.success(request, f"Your Event {format(update_form)} has been updated.")
				return render(request, 'events/event_details.html', {"event_details": event_details,})
		# TODO : Add JS popup denoting that changes are invalid.
		else:
			update_form = EventCreationForm(instance=event_details)
	# Route user to event details if they aren't the host.
	# TODO Add JavaScript popup message saying user is unauthorized to edit event information
	else:
		context = {"event_details": event_details,}
		return render(request, 'events/event_details.html', context)

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
