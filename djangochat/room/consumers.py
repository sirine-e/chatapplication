import json

from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Room, Message

#define a WebSocket consumer to handle chat functionality
class ChatConsumer(AsyncWebsocketConsumer):

    # Method called when a WebSocket connection is established
    async def connect(self):
        # Extract the room_name from the URL parameters
        self.room_name = self.scope['url_route']['kwargs']['room_name']
         # Formulate a unique group name for the room
        self.room_group_name = 'chat_%s' % self.room_name

        # Add the channel to the group corresponding to the room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        #accept the Websocket connection
        await self.accept()

    # Method called when a WebSocket connection is closed
    async def disconnect(self, close_code):
        # Remove the channel from the group when the connection is closed
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        # Parse the received JSON data
        data = json.loads(text_data)
        print(data)
        # Extract message, username, and room from the data
        message = data['message']
        username = data['username']
        room = data['room']

        # Save the received message to the database
        await self.save_message(username, room, message)

        # Send the received message to the entire room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username
            }
        )

    # Method called when a message is received from the room group
    async def chat_message(self, event):
        # Extract message and username from the received event
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))


    # Method to save a message to the database asynchronously
    @sync_to_async
    def save_message(self, username, room, message):
        # Get the user and room objects from the database
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        # Get the user and room objects from the database
        Message.objects.create(user=user, room=room, content=message)