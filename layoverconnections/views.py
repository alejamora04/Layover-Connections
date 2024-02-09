from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import NewUserForm, UserUpdateForm, ProfileUpdateForm, ImageUploadForm
from django.contrib.auth.models import User
from .models import Profile


# [User Login & Registration] Views.

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
			# Create Profile to add one-to-one to the newly registered User.
			new_user_profile = Profile.objects.create(user = request.user)
			new_user_profile.save()
			messages.success(request, "Registration successful.")
			return redirect("layoverconnections:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="layoverconnections/register.html", context={"register_form":form})

# View functionality for user log in. 
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


# [User Profile] Views
# User profile routing & CRUD Operations

# [CRUD] - Read Operations
# Route to logged_in user's profile
@login_required
def user_profile(request):
	return render(request, 'layoverconnections/user_profile.html')

# Route to a specific user's public profile via their id.
@login_required
def public_profile(request, user_id):
	queried_user = User.objects.get(id = user_id) 
	
	context = {
		"queried_user": queried_user,
	}
	return render(request, 'layoverconnections/public_profile.html', context)


# [CRUD] - Update Operations
# Update User Profile information
@login_required
def edit_profile(request, user_profile_id):
	# Query user profile based on logged in user
	current_user = request.user
	user_profile_id = current_user.id
	queried_profile = Profile.objects.get(user = current_user)

	# Validate that current user is the owner of the user profile to allow editing.
	if queried_profile.user.id == user_profile_id:
		if request.method == "POST":
			u_form = UserUpdateForm(request.POST, instance=request.user)
			p_form = ProfileUpdateForm(request.POST, 
									request.FILES, 
									instance=request.user.profile)
			if u_form.is_valid() and p_form.is_valid():
				u_form.save()
				p_form.save()

				return render(request, 'layoverconnections/user_profile.html', messages.success(request, f"Your account has been updated.") )

		else:
			u_form = UserUpdateForm(instance=request.user)
			p_form = ProfileUpdateForm(instance=request.user.profile)

		context = {
			'u_form': u_form,
			'p_form': p_form
		}
		# Update profile information and display it to the user.
		return render(request, 'layoverconnections/edit_profile.html', context)
	
	# Return user to Log-In if validation fails display message of invalid credentials.
	return render(request, "layoverconnections/login.html",
		messages.info(request, "Invalid Credentials.") )

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

# CRUD - Delete Operations
# Allow user to delet their profile and user account
@login_required
def delete_profile(request):
	# Query user profile based on logged in user
	current_user = request.user
	profile_to_delete = Profile.objects.get(user = current_user)
	user_to_delete = User.objects.get(username = current_user.username)
	
	context = {
		"delete_profile": profile_to_delete,
	}

	if request.method == "POST":
		profile_to_delete.delete()
		user_to_delete.delete()

		return render(request, 'layoverconnections/login.html')
	
	return render(request, 'layoverconnections/delete_profile.html', context)

# Homepage Based Views

# Configure Requests for the homepage http request
def homepage(request):
	return render(request, 'layoverconnections/homepage.html')


#  path("events", views.create_event, name="events")
# Routing to a user profile.
@login_required
def create_event(request):
	return render(request, 'layoverconnections/events.html')