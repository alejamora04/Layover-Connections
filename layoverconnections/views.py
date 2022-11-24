from django.shortcuts import render
from django.http import HttpResponse

# Create the formatting for the home page here.
def index(request):
    return render(request, 'layoverconnections/index.html')

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