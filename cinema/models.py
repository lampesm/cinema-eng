from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    status = models.IntegerField()


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


class Chair(models.Model):
    number = models.IntegerField()
    availability = models.BooleanField(default=True)
    show = models.DateTimeField(auto_now=False, auto_now_add=False)
    cinema_room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Program(models.Model):
    cinema_room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    show = models.DateTimeField(auto_now=False, auto_now_add=False)


class Reservation(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
