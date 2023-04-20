from django.forms import ModelForm
from .models import *
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']


class UserForm(ModelForm):
    class Meta:
        model=ProfileModel
        fields='__all__'
        exclude=['name']
        

    

