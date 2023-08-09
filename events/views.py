from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event
from .forms import EventCreationForm, EventUpdateForm
# Enables Datetime objects to become aware
from django.utils import timezone


# Formatting for the splash page portal. 
#TODO Setup the splash page with a demo button to - return render(request, 'layoverconnections/index.html')
# Base Event Page to encapsulate all event controls.
def event_base(request):
	return render(request, 'events/event_splashpage.html')

# Load form variables for the event creation portal.
@login_required 
def create_event(request):
	if request.method == 'POST':
		Event_Form = EventCreationForm(request.POST)
		Event_Form.instance.host = request.user
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


# Render single event details Allow the host to edit and for guest to join.
def event_details(request, event_id):
	event_details = get_object_or_404(Event, pk = event_id)

	context = {
		"event_details": event_details,
	}

	return render(request, 'events/event_details.html', context)



# Placeholder for Host Modify events
def edit_event(request, event_id):
	event_details = get_object_or_404(Event, pk = event_id)

	if request.method == "POST":
		update_form = EventUpdateForm(request.POST, instance=request.user)
		if update_form.is_valid():
			update_form.save()
			messages.success(request, f"Your Event has been updated")
			return render(request, 'events/even_details.html', {"event_details": event_details})
	
	else:
		update_form = EventUpdateForm(instance=request.user)

	context = {
		"event_details": event_details,
		"update_form": update_form,
	}
		 

	return render(request, 'events/edit_event.html', context)



"""
# Update User Profile information
@login_required
def edit_profile(request):
	if request.method == "POST":
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
								   request.FILES, 
								   instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f"Your account has been updated.") 
			return render(request, 'layoverconnections/user_profile.html')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'layoverconnections/edit_profile.html', context)



"""











# [END GOAL] Front-End: Formatted Front-End UI heavy event creation
def end_product(request):
	return render(request, 'events/event_frontend.html')
