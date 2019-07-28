from django.urls import path, re_path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name = 'connections/login.html')), 
    path('logout/', LoginView.as_view(template_name = 'connections/logout.html')),
    path('register/', views.register, name='register')
]