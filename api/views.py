from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView

from cinema.models import Program, Chair
from .serializer import ProgramSerializer, ChairSerializer


class ProgramUpdateView(RetrieveUpdateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


class ChairUpdateView(RetrieveUpdateAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer


class ChairReadView(RetrieveAPIView):
    queryset = Chair.objects.all()
    serializer_class = ChairSerializer