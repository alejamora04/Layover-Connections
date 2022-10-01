from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

# Create the formatting for the home page here.
def index(request):
    return HttpResponse("Hello placeholder text")

# Set up the formatting for the welcome page.
def login(request):
    return render(request, 'homepage/login.html')

# URL routing to a name 
def hello_there(request, name):
    return render(
        request,
        'homepage/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    ) 