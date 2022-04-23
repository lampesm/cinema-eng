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
from .permissions import (
    IsSuperUserOrStaffReadOnly, 
    IsStaffOrReadOnly, 
)


class ProgramUpdateView(RetrieveUpdateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (IsStaffOrReadOnly, )


# -----------------------------------
class ChairUpdateView(RetrieveUpdateAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer
    permission_classes = (IsStaffOrReadOnly, )


# --------------------------------------------
class MoiveListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsStaffOrReadOnly, )


class MoiveGetView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsStaffOrReadOnly, )


class MoiveUpdateView(RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsStaffOrReadOnly, )


class MoiveDeleteView(RetrieveDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )


class MoivePostView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsStaffOrReadOnly, )

# ------------------------------------------------
class CinemaRoomListView(ListAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer
    permission_classes = (IsStaffOrReadOnly, )


class CinemaRoomGetView(RetrieveAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer
    permission_classes = (IsStaffOrReadOnly, )


class CinemaRoomUpdateView(RetrieveUpdateAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer
    permission_classes = (IsStaffOrReadOnly, )


class CinemaRoomDeleteView(RetrieveDestroyAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer
    permission_classes = (IsSuperUserOrStaffReadOnly, )


class CinemaRoomPostView(CreateAPIView):
    queryset = CinemaRoom.objects.all()
    serializer_class = CinemaRoomSerializer
    permission_classes = (IsStaffOrReadOnly, )
