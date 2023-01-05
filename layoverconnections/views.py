from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.decorators import login_required

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

# Configure Requests for the homepage http request
def homepage(request):
	return render(request, 'layoverconnections/homepage.html')


"""
def user_profile(request, name):
    return render(
        request,
        'layoverconnections/user_profile.html',
        {
            'name': name,
        }
    ) 

"""