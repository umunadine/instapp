from django import forms
from .models import Profile

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date_posted','profile','like']