from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    numbers = [1,2,3,4,5]
    name = "Alex"

    args = {'myName': name, 'numbers': numbers}
    return render(request, 'connections/home.html', args)

def login(request):
    # form = NewUserRegistrationForm(request.POST or None)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/Login/") 
    #     else:
    #         form = NewUserRegistrationForm()
    return render(request, 'connections/login.html')

    # {'form': form} 


# need to create a login function that works properly