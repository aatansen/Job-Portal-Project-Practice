from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import *
from django.forms.widgets import PasswordInput

class Custom_user_form(UserCreationForm):
    class Meta:
        model=Custom_user_model
        fields=['username','User_Type','Gender','City','Profile_Picture']
        help_texts={
            'username':None
        }

class Auth_form(AuthenticationForm):
    class Meta:
        model=Custom_user_model
        fields=['username','password']
        

