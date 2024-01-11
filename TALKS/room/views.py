from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RoomCreationForm
from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = list(Message.objects.filter(room=room).order_by('-id')[:25])[::-1]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})


def create_room(request):
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)
        if form.is_valid():
            room = form.save()
            # Redirect to the room detail page or chat page
            messages = list(Message.objects.filter(room=room).order_by('-id')[:25])[::-1]
            return render(request, 'room/room.html', {'room': room, 'messages': messages})
    else:
        form = RoomCreationForm()

    return render(request, 'room/create_room.html', {'form': form})