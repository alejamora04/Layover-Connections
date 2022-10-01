from django.shortcuts import render
from django.http import HttpResponse

# Create the formatting for the home page here.
def home(request):
    return HttpResponse("Hello placeholder text")

# Placeholder Template 
def hello_there(request, name):
    return render(
        request,
        'homepage/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    ) 