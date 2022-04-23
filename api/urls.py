from django.urls import path

from .views import (
    ProgramUpdateView, 
    ChairUpdateView, 
    MoiveDeleteView, 
    MoiveGetView,
    MoiveListView,
    MoivePostView, 
    MoiveUpdateView,
    CinemaRoomDeleteView, 
    CinemaRoomGetView,
    CinemaRoomListView,
    CinemaRoomPostView, 
    CinemaRoomUpdateView,
)


app_name = 'api'

urlpatterns = [
    path('v1/program/update/<int:pk>', ProgramUpdateView.as_view(), name='program_update'),

    path('v1/chair/update/<int:pk>', ChairUpdateView.as_view(), name='chair_update'),

    path('v1/movie/get/', MoiveListView.as_view(), name='list_movie'),
    path('v1/movie/get/<int:pk>', MoiveGetView.as_view(), name='get_movie'),
    path('v1/movie/delete/<int:pk>', MoiveDeleteView.as_view(), name='delete_movie'),
    path('v1/movie/update/<int:pk>', MoiveUpdateView.as_view(), name='update_movie'),
    path('v1/movie/post/', MoivePostView.as_view(), name='post_movie'),

    path('v1/cinemaroom/get/', CinemaRoomListView.as_view(), name='list_cinemaroom'),
    path('v1/cinemaroom/get/<int:pk>', CinemaRoomGetView.as_view(), name='get_cinemaroom'),
    path('v1/cinemaroom/delete/<int:pk>', CinemaRoomDeleteView.as_view(), name='delete_cinemaroom'),
    path('v1/cinemaroom/update/<int:pk>', CinemaRoomUpdateView.as_view(), name='update_cinemaroom'),
    path('v1/cinemaroom/post/', CinemaRoomPostView.as_view(), name='post_cinemaroom'),
]