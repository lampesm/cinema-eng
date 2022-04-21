from django.views.generic import ListView

from . models import CinemaRoom


class CinemaRoomView(ListView):
    def get_queryset(self):
        return CinemaRoom.objects.all()
    