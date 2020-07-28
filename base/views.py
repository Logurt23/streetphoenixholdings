from django.shortcuts import render
from datetime import date
from .forms import *

def success(request):
    return HttpResponse('successfully uploaded')

# Tailwinds CSS homepage
def homepage(request):
    left = Upload.objects.all()[:3]
    middle = Upload_two.objects.all()[:3]
    right = Upload_three.objects.all()[:3]
    return render(request, 'base/homepage.html', context={
        'left': left,
        'middle': middle,
        'right': right,
    })

# Bootstrap Homepage
def bootstrap(request):

    this_year = date.today().year

    return render(request, 'bootstrap/bootstrap.html', context={
        'year': this_year,
    })
