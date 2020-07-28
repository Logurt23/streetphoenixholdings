# forms.py
from django import forms
from .models import *

class ImageFormLeft(forms.ModelForm):

    class Meta:
        model = Upload
        fields = ['title', 'left_images']

class ImageFormMiddle(forms.ModelForm):

    class Meta:
        model = Upload_two
        fields = ['title', 'middle_images']

class ImageFormRight(forms.ModelForm):

    class Meta:
        model = Upload_three
        fields = ['title', 'right_images']
