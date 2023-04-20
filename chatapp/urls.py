from django.urls import path
from .views import *


urlpatterns=[

    path('',home,name='home'),
    
    
    path('register',register,name='register'),

    path('login-register/',loginPage,name='login'),

    path('logout/',logoutuser,name='log-out'),

    path('room/<int:id>',room,name='room'),

    path('profile/<int:id>',userprofile,name='user-profile'),

    path('create-room/',createroom,name='create-room'),

    path('update-room/<int:id>/',updateroom,name='update-room'),
    
    path('delete-room/<int:id>/',deleteroom,name='delete-room'),

    path('delete-message/<int:id>/',deletemessage,name='delete-message'),
    
    path('update-user/<int:id>/',updateuser,name='update-user'),

    path('topics/',topicspage,name='topics'),

    path('activity/',activitypage,name='activity'),


]