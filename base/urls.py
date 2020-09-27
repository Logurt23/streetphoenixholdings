from django.urls import path
from .views import homepage, events

# base App urls

urlpatterns = [
    path('', homepage, name='homepage'),
    path('events/', events, name='events'),
]
