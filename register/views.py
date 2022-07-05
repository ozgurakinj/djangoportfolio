from django.shortcuts import render
from main.models import Profile
from main.views import user
from .forms import RegisterForm
from django.shortcuts import redirect
from django.contrib import messages
from .models import *

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user, username=user.username, name=user.first_name + " " +user.last_name)
            profile.save()
            print(profile)
            messages.success(response, "Registration successful. Now you can login")
        else:
            messages.error(response, str(form.errors.as_json()))
        return redirect('/register')
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})