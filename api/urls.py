from django.urls import path

from .views import ProgramUpdateView, ChairUpdateView, ChairReadView


app_name = 'api'

urlpatterns = [
    path('v1/program/update/<int:pk>', ProgramUpdateView.as_view(), name='program_update'),
    path('v1/chair/update/<int:pk>', ChairUpdateView.as_view(), name='chair_update'),
    path('v1/chair/read/<int:pk>', ChairReadView.as_view(), name='chair_read'),
]