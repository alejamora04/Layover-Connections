from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

# Create the formatting for the home page here.
def index(request):
    return render(request, 'layoverconnections/index.html')

# Set up the formatting for the welcome page.
def login(request):
    return render(request, 'layoverconnections/login.html')

# URL routing to a name 
def user_profile(request, name):
    return render(
        request,
        'layoverconnections/user_profile.html',
        {
            'name': name,
            'date': datetime.now()
        }
    ) 