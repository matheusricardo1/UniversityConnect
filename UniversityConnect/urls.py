from django.urls import path
from . import views

app_name = 'UniversityConnect'

urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('cursos/', views.cursos, name='cursos'),
   path('cursos/<int:id>', views.cursos_detail, name='cursos_detail'),
   path('accounts/profile/', views.profile, name='profile'),
]
