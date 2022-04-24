from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


from .models import Movie, CinemaRoom, Chair, Program, Reservation


class MovieAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'director', 'duration', 'poster')
    list_filter = ('director',)
    search_fields = ('name', 'director')


class CinemaRoomAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ChairAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('number', 'salesـstatus', 'program')
    list_filter = ('salesـstatus',)


class ProgramAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cinema_room', 'movie', 'status', 'show',)
    list_filter = ('cinema_room', 'show', 'status',)
    search_fields = ('cinema_room', 'movie',)


class ReservationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'program', 'chair',)


admin.site.register(Movie, MovieAdmin)
admin.site.register(CinemaRoom, CinemaRoomAdmin)
admin.site.register(Chair, ChairAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Reservation, ReservationAdmin)