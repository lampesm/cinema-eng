from django.shortcuts import get_object_or_404
from django.views.generic import ListView, UpdateView
from django.views.generic.edit import FormView

from .models import CinemaRoom, Program, Chair


class CinemaRoomView(ListView):
    context_object_name = 'cinema_object'

    def get_queryset(self):
        return CinemaRoom.objects.all()


class ProgramView(ListView):
    context_object_name = 'program_object'

    def get_queryset(self):
        cinema_room_id = self.kwargs.get('cinema_room_id')
        return Program.objects.filter(cinema_room_id=cinema_room_id)


class ChairView(ListView):
    context_object_name = 'chair_object'

    def get_queryset(self):
        program_id = self.kwargs.get('program_id')
        return Chair.objects.filter(program_id=program_id)


class UpdateChiarView(UpdateView):
    model = Chair
    fields = ['number', 'availability'] 
    template_name = 'cinema/update_status_chair.html' 
    success_url="/"
