# /football/frontend/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login, {'template_name': 'football/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'football/logout.html'}, name='logout'),

]