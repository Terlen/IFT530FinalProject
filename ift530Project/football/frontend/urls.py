# /football/frontend/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login, {'template_name': 'football/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'football/logout.html'}, name='logout'),
    path('registerplayer/', views.register_player, name='registerplayer'),
    path('registerteam/', views.register_team, name='registerteam'),
    path('registerstadium/', views.register_stadium, name='registerstadium'),
    path('registermatch/', views.register_match, name='registermatch'),
    path('registerroster/', views.register_roster, name='registerroster'),
    path('registerstat/', views.register_stat, name='registerstat'),
    path('registerscore/', views.register_score, name='registerscore'),
    path('viewplayer/', views.view_player, name='viewplayer'),
    path('viewteam/', views.view_team, name='viewteam'),
    path('viewstadium/', views.view_stadium, name='viewstadium'),
    path('viewmatch/', views.view_match, name='viewmatch'),
    path('viewroster/', views.view_roster, name='viewroster'),
    path('viewstat/', views.view_stat, name='viewstat'),
    path('viewscore/', views.view_score, name='viewscore'),
]