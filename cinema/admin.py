from django.contrib import admin

from .models import MyUser, Movie, CinemaRoom, Chair, Program, Reservation


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'mobile', 'status',)
    list_filter = ('status',)
    search_fields = ('username', 'mobile')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'duration', 'poster')
    list_filter = ('duration',)
    search_fields = ('name', 'director')


class CinemaRoomAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ChairAdmin(admin.ModelAdmin):
    list_display = ('number', 'availability', 'program')
    list_filter = ('availability',)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('cinema_room', 'movie', 'status', 'show',)
    list_filter = ('cinema_room', 'show', 'status',)
    search_fields = ('cinema_room', 'movie',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'program', 'chair',)


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(CinemaRoom, CinemaRoomAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Reservation, ReservationAdmin)