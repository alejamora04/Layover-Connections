from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages

# Create the formatting for the home page here.
def index(request):
    return render(request, 'layoverconnections/index.html')

# Server side new user registration validation
# consider changing layoverconnections/register on urls.py
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST) 
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("layoverconnections/login.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="layoverconnections/register.html", context={"register_form":form})

# Set up the formatting for the welcome page.
def login(request):
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