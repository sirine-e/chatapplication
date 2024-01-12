from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RoomCreationForm
from .models import Room, Message


@login_required
def rooms(request):
    #Retrieve the rooms from database
    rooms = Room.objects.all()
    #Render room.html template with the list of rooms
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    #Retrieve the room based on the provided slug from the url
    room = Room.objects.get(slug=slug)
    #Retrieve and order the latest 25 messages of the room
    messages = list(Message.objects.filter(room=room).order_by('-id')[:25])[::-1]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})


def create_room(request):
    #Only if the user post the form
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            room = form.save()
            messages = list(Message.objects.filter(room=room).order_by('-id')[:25])[::-1]
            return render(request, 'room/room.html', {'room': room, 'messages': messages})
    else:
        #Display the empty form
        form = RoomCreationForm()

    return render(request, 'room/create_room.html', {'form': form})