from django.urls import path, include, re_path

from .views import CinemaRoomView, ProgramView, ChairView

app_name = 'cinema'

urlpatterns = [
    path('', CinemaRoomView.as_view(), name='home'),
    path('program/<int:cinema_room_id>', ProgramView.as_view(), name='program'),
    path('program/chair/<int:program_id>', ChairView.as_view(), name='chair'),
]