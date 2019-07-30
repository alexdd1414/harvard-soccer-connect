from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import (
    RegistrationForm,
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('connections:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'connections/reg_form.html', args)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'connections/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('connections:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'connections/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('connections:view_profile'))
        else:
            return redirect(reverse('connections:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'connections/change_password.html', args)



# from django.shortcuts import render, redirect
# from django.urls import reverse

# from .forms import (
#     RegistrationForm,
#     EditProfileForm
# )

# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
# # from django.contrib.auth import update_session_auth_hash
# # from django.contrib.auth.decorators import login_required

# # from django.views.generic.base import TemplateView
# from .models import Player

# def home(request):
#         numbers = [1,2,3,4,5]
#         name = "Alex"

#         args = {'myName': name, 'numbers': numbers}
#         return render(request, 'connections/home.html', args)

# def register(request):
#     if request.method =='POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # args = {'user': request.user}
#             # return render(request, 'connections/reg_form.html', args)
#             return redirect('/connections/profile')
#             # return render(request, 'connections/profile.html', {'form': form})
#         else:
#             print('testing')
#             print(form.errors)
#             return render(request, 'connections/error.html')

#     else:
#         form = RegistrationForm()

#         args = {'form': form}
#         return render(request, 'connections/reg_form.html', args)

# def view_profile(request):
#         args = {'user': request.user}
#         return render(request, 'connections/profile.html', args)

# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)

#         if form.is_valid():
#             form.save()
#             return redirect ('/connections/profile')
#             # args = {'user': request.user}
#             # return render(request, 'connections/profile.html', args)
#     else:
#         form = UserChangeForm(instance=request.user)
#         args = {'form:':form}
#         return render(request, 'connections/edit_profile.html', args)

