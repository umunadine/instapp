from django.shortcuts import render
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Post,Comment,Follow,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewCommentForm, AddProfileForm
from django.contrib.auth.models import User

def signup(request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                new_profile = Profile(user=user)
        else:
            form = SignupForm()
    return render(request, 'registration/registration_form.html',{'form':form})
