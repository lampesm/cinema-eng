from django.urls import path

from .views import (
    ProgramUpdateView, 
    ChairUpdateView, 
    MoiveDeleteView, 
    MoiveGetView,
    MoiveListView,
    MoivePostView, 
    MoiveUpdateView
)


app_name = 'api'

urlpatterns = [
    path('v1/program/update/<int:pk>', ProgramUpdateView.as_view(), name='program_update'),
    path('v1/chair/update/<int:pk>', ChairUpdateView.as_view(), name='chair_update'),
    path('v1/movie/get/', MoiveListView.as_view(), name='list_movie'),
    path('v1/movie/get/<int:pk>', MoiveGetView.as_view(), name='get_movie'),
    path('v1/movie/delete/<int:pk>', MoiveDeleteView.as_view(), name='delete_movie'),
    path('v1/movie/update/<int:pk>', ChairUpdateView.as_view(), name='update_movie'),
    path('v1/movie/post/', MoivePostView.as_view(), name='post_movie'),
]