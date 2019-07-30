# from django.urls import path, re_path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', LoginView.as_view(template_name = 'connections/login.html')), 
#     path('logout/', LoginView.as_view(template_name = 'connections/logout.html')),
#     path('register/', views.register, name='register'),
#     path('profile/', views.view_profile, name='view_profile'),
#     path('profile/edit/', views.edit_profile, name='edit_profile')
# ]

from django.contrib import admin
from django.urls import path, include # new
from . import views
from django.conf.urls import url
# from django.views.generic.base import TemplateView 


# from django.urls import path, re_path, include

# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import (
#     LoginView, LogoutView, password_reset, password_reset_done, password_reset_confirm,
#     password_reset_complete
# )

urlpatterns = [ 
    # url(r'^register/$', views.register, name='register'),
    path('register/', views.register, name='register'),  
    # path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    # url(r'^profile/$', views.view_profile, name='view_profile'),
    path('', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    # url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'), 
    # url(r'^change-password/$', views.change_password, name='change_password'), 
    url('change_password', views.change_password, name='change_password'),  
    path('admin/', admin.site.urls),
    path('connections/', include('django.contrib.auth.urls')), # new
    
]
#     url(r'^login/$', auth_views.login, {'template_name': 'connections/login.html'}, name='login'),
#     url(r'^logout/$', auth_views.logout, {'template_name': 'connections/logout.html'}, name='logout'),
#     # path('login/', LoginView.as_view(template_name = 'connections/login.html')), 
#     # path('logout/', LoginView.as_view(template_name = 'connections/logout.html')),
#     # path('connections/', include('django.contrib.auth.urls')),
#     url(r'^register/$', views.register, name='register'),
#     url(r'^profile/$', views.view_profile, name='view_profile'),
#     url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
#     url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
#     url(r'^change-password/$', views.change_password, name='change_password'),

#     url(r'^reset-password/$', auth_views.password_reset, {'template_name': 'connections/reset_password.html', 'post_reset_redirect': 'connections:password_reset_done', 'email_template_name': 'connections/reset_password_email.html'}, name='reset_password'),

#     url(r'^reset-password/done/$', auth_views.password_reset_done, {'template_name': 'connections/reset_password_done.html'}, name='password_reset_done'),

#     url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'template_name': 'connections/reset_password_confirm.html', 'post_reset_redirect': 'connections:password_reset_complete'}, name='password_reset_confirm'),

#     url(r'^reset-password/complete/$', auth_views.password_reset_complete,{'template_name': 'connections/reset_password_complete.html'}, name='password_reset_complete')
# ]