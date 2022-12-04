from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Configure formatting for the home page here.
def index(request):
	if not request.user.is_authenticated:
		return redirect(reverse("layoverconnections:login"))
	return render(request, 'layoverconnections/index.html')

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

# Set up the formatting for the welcome page. email = request.POST["email"]
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

# Routing to a user profile. 
def user_profile(request, name):
    return render(
        request,
        'layoverconnections/user_profile.html',
        {
            'name': name,
        }
    ) 

# Configure Requests for the homepage http request
def homepage(request):
	return render(request, 'layoverconnections/homepage.html')