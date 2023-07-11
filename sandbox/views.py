from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Event
from .forms import EventCreationForm

# Formatting for the splash page portal. 
#TODO Setup the splash page with a demo button to - return render(request, 'layoverconnections/index.html')
def index(request):
	return render(request, 'sandbox/sandbox_placeholder.html')

# Base Event Page to encapsulate all event controls.
def event_base(request):
	return render(request, 'sandbox/event.html')


# TODO Link to the event.py to check duration and other python driven controls.
# [PROTOTYPE] Formatting for the Event page. 
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
    context = {
        "Events": event_list
    }
    return render(request, 'sandbox/existing_event.html', context)


# [END GOAL] Front-End: Formatted Front-End UI heavy event creation
def end_product(request):
	return render(request, 'sandbox/event_frontend.html')








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

# Update About Me Section
@login_required
def edit_bio(request):
	if request.method == "POST":
		aboutme_form = AboutMeForm(request.POST, 
								   request.FILES, 
								   instance=request.user.profile)
		picture_form = ImageUploadForm(request.POST, 
										request.FILES, 
										instance=request.user.profile)
		if aboutme_form.is_valid() and picture_form.is_valid():
			aboutme_form.save()
			picture_form.save()
			messages.success(request, f"Your bio has been updated.") 
			return render(request, 'layoverconnections/user_profile.html')

	else:
		aboutme_form = AboutMeForm(instance=request.user.profile)
		picture_form = ImageUploadForm(instance=request.user.profile)


	context = {
		'aboutme_form': aboutme_form,
		'picture_form': picture_form
	}

	return render(request, 'layoverconnections/about_me.html', context)


"""