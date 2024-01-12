from django.urls import path

from . import consumers

#The websocket connection will be established with a specific room identified by its name
websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]