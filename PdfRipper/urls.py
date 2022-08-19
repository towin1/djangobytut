from django.urls import path
from . import views



urlpatterns = [
  path('PDFRIp', views.PDFRIp, name='PDFRIp'),
]