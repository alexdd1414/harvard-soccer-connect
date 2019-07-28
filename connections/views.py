from django.shortcuts import render, redirect
# from django.http import HttpResponse,
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


# from django.views.generic.base import TemplateView
from .models import Player

def home(request):
    numbers = [1,2,3,4,5]
    name = "Alex"

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'connections/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/connections')
    else:
        form = RegistrationForm()
        
        args = {'form': form}
        return render(request, 'connections/reg_form.html', args)



# need to create a login function that works properly