from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    duration = models.DurationField()
    poster = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name


class CinemaRoom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Program(models.Model):
    cinema_room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    show = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.cinema_room} {self.movie} {self.status} {self.show}'


class Chair(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, default=None)
    number = models.IntegerField()
    salesـstatus = models.BooleanField(default=False)

    def __str__(self):
        return f' {self.program} {self.number}'
