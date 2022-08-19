from django.urls import path
from . import views



urlpatterns = [
  path('CSVrip', views.CSVrip, name='CSVrip'),
]