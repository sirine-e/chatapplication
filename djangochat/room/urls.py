from django.urls import path
from .views import create_room, user_list
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/<slug:slug>/', views.room, name='room'),
    path('create_room/', create_room, name='create_room'),
    path('user_list/', user_list, name='user_list'),
]