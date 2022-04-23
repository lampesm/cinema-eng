from rest_framework import serializers

from cinema.models import Program, Chair, Movie, CinemaRoom


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class ChairSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaRoom
        fields = '__all__'