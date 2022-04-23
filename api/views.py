from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateAPIView, 
    RetrieveAPIView, 
    RetrieveDestroyAPIView, 
    CreateAPIView,
    ListAPIView
)

from cinema.models import Program, Chair, Movie, CinemaRoom
from .serializer import (
    ProgramSerializer, 
    ChairSerializer, 
    MovieSerializer, 
    CinemaRoomSerializer
)


class ProgramUpdateView(RetrieveUpdateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ChairUpdateView(RetrieveUpdateAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer


class MoiveListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoiveGetView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoiveUpdateView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoiveDeleteView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoivePostView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer










class CinemaRoomListView(ListAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer


class CinemaRoomGetView(RetrieveAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer


class CinemaRoomUpdateView(RetrieveUpdateAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer


class CinemaRoomDeleteView(RetrieveDestroyAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer


class CinemaRoomPostView(CreateAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer
