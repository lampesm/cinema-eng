from django.views.generic import ListView, UpdateView
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .models import CinemaRoom, Program, Chair
from .forms import NewUserForm


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
    fields = ['salesـstatus'] 
    template_name = 'cinema/update_status_chair.html' 
    success_url="/"


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("cinema:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})