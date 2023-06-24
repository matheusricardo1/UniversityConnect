from django.urls import path
from . import views

app_name = 'UniversityConnect'

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('cursos/', views.cursos, name='cursos'),
]
