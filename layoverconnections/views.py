from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm, ImageUploadForm

# from django.urls import reverse
# from .models import Profile

# Login Registration and Sign Up Views.

# Splash page routing
def index(request):
	if not request.user.is_authenticated:
		return render(request, "layoverconnections/splashpage.html")
	return render(request, 'layoverconnections/homepage.html')

# New user registration validation
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST) 
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("layoverconnections:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="layoverconnections/register.html", context={"register_form":form})

# Formatting for the Login page. 
# TODO change username field to email- register form email = request.POST["email"]
def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"] 
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("layoverconnections:homepage")
		else:
			return render(request, "layoverconnections/login.html",
				messages.info(request, "Invalid Credentials.") )
	return render(request, 'layoverconnections/login.html')

# Logout Functionality
def logout_request(request):
	logout(request)
	return render(request, "layoverconnections/login.html",
		messages.info(request, "You have Succesfully logged out.") )


# User Profile Based Views

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

	return render(request, 'layoverconnections/edit_profile.html', context)# TODO Route back to Login Page.

# Update About Me Section
@login_required
def edit_bio(request):
	if request.method == "POST":
		profile_form = ProfileUpdateForm(request.POST, 
								   request.FILES, 
								   instance=request.user.profile)
		picture_form = ImageUploadForm(request.POST, 
										request.FILES, 
										instance=request.user.profile)
		if profile_form.is_valid() and picture_form.is_valid():
			profile_form.save()
			picture_form.save()
			messages.success(request, f"Your bio has been updated.") 
			return render(request, 'layoverconnections/user_profile.html')

	else:
		profile_form = ProfileUpdateForm(instance=request.user.profile)
		picture_form = ImageUploadForm(instance=request.user.profile)


	context = {
		'profile_form': profile_form,
		'picture_form': picture_form
	}

	return render(request, 'layoverconnections/about_me.html', context)

# Homepage Based Views

# Configure Requests for the homepage http request
def homepage(request):
	return render(request, 'layoverconnections/homepage.html')


#  path("events", views.create_event, name="events")
# Routing to a user profile.
@login_required
def create_event(request):
	return render(request, 'layoverconnections/events.html')