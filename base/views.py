from django.shortcuts import render
from datetime import date
from .forms import *

def success(request):
    return HttpResponse('successfully uploaded')

# Tailwinds CSS homepage
def homepage(request):
    return render(request, 'base/homepage.html', context={

    })

# Bootstrap Homepage
def events(request):

    return render(request, 'base/events.html', context={

    })
