from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    numbers = [1,2,3,4,5]
    name = "Alex"

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'connections/home.html', args)

def login(request):
    return render(request, 'connections/login.html')


# need to create a login function that works properly