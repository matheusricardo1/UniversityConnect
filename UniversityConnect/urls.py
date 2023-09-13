from django.urls import path
from . import views

app_name = 'UniversityConnect'

urlpatterns = [
   
   path('', views.homepage, name='homepage'),
   path('courses/', views.courses, name='courses'),
   path('courses/<int:id>', views.courses_detail, name='courses_detail'),
   path('accounts/profile/', views.profile, name='profile'),
]


