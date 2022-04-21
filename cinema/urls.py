from django.urls import path, include

from .views import CinemaRoomView

app_name = 'cinema'

urlpatterns = [
    path('', CinemaRoomView.as_view(), name='list'),
]