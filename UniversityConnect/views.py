from django.shortcuts import render
#from models 

def homepage(request):
    return render(request, 'UniversityConnect/html/pt/index.html')

def cursos(request):
    return render(request, 'UniversityConnect/html/pt/cursos.html')