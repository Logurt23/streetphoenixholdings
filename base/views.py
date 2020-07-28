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
def bootstrap(request):

    this_year = date.today().year

    return render(request, 'bootstrap/bootstrap.html', context={
        'year': this_year,
    })
