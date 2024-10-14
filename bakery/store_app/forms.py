from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            # 'bio',
            'user',
            'phone',
            # 'birth_date',
            'address',
            'profile_image'
        ]



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'rating']



"""
class EditUserProfileForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','phone','address']
        labels = {'email':'Email'}
        
class EditAdminProfileForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Email'}
"""