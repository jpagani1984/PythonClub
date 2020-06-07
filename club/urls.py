from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getmeetings/', views.getmeetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='meetingdetails'),
    path('newMeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]