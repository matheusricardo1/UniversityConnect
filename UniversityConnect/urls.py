from django.urls import path
from . import views

app_name = 'UniversityConnect'

urlpatterns = [
   
   path('', views.homepage, name='homepage'),
   path('courses/', views.courses, name='courses'),
   path('courses/<int:id>', views.courses_detail, name='courses_detail'),
   path('accounts/profile/', views.profile, name='profile'),
   path('history/', views.history, name="history"),
   path('history/ex_students/', views.ex_students, name="ex_students"),
   path('places/', views.places, name="places"),
]


