from django.urls import path
from . import views

app_name = 'UniversityConnect'

urlpatterns = [
   path('', views.homepage, name='homepage'),
]
