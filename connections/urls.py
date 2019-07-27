from django.urls import path, re_path
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import login
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # re_path(r'^login/$', views.login, name='login')
    path('login/', views.login, name="login")
    # url('', login, {'template_name': 'connections/login.html'})
    # url(r'^login/$', login, {'template_name': 'connections/login.html'})
]

