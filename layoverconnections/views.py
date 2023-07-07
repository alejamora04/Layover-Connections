from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Event
from django.contrib import messages
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm, AboutMeForm, ImageUploadForm

# Formatting for the splash page portal. 
#TODO Setup the splash page with a demo button to - return render(request, 'layoverconnections/index.html')
def index(request):
	if not request.user.is_authenticated:
		return redirect(reverse("layoverconnections:login"))
	return render(request, 'layoverconnections/homepage.html')

# Server side new user registration validation
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST) 
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("layoverconnections:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="layoverconnections/register.html", context={"register_form":form})

# Formatting for the Login page. 
# TODO change username field to email- register form email = request.POST["email"]
# TODO Fix Django populated error messages
# TODO Fix Redirect after user registers and signs in
def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"] 
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("layoverconnections:homepage")
		else:
			return render(request, "layoverconnections/index.html", {
				"message": "Invalid Credentials."
			})
	return render(request, 'layoverconnections/login.html')

# Logout Functionality
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("layoverconnections:index")

# Routing to a user profile.
@login_required
def user_profile(request):
	return render(request, 'layoverconnections/user_profile.html')

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

# Configure Requests for the homepage http request
def homepage(request):
	return render(request, 'layoverconnections/homepage.html')


#  path("events", views.create_event, name="events")
# Routing to a user profile.
@login_required
def create_event(request):
	return render(request, 'layoverconnections/events.html')