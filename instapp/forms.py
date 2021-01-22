from django import forms
from .models import Profile

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']