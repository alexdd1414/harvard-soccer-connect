from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import (
    RegistrationForm,
#     EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.decorators import login_required

# from django.views.generic.base import TemplateView
from .models import Player

def home(request):
        numbers = [1,2,3,4,5]
        name = "Alex"

        args = {'myName': name, 'numbers': numbers}
        return render(request, 'connections/home.html', args)

# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/connections')
#         else: 
#             return render(request, 'connections/login.html', {}) 
#     else:
#         form = RegistrationForm()

#         args = {'form': form}
#         return render(request, 'connections/reg_form.html', args)


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'connections/profile.html', {'form': form})
        else:
            print('testing')
            print(form.errors)
            return render(request, 'connections/error.html')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'connections/reg_form.html', args)

def profile(request):
        args = {'user': request.user}
        return render(request, 'connections/profile.html', args)
