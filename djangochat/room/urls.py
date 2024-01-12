from django.urls import path
from .views import create_room
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('room/<slug:slug>/', views.room, name='room'),
    path('create_room/', create_room, name='create_room'),
]