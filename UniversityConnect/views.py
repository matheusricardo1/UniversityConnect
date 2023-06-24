from django.shortcuts import render
#from models 

def homepage(request):
    return render(request, 'UniversityConnect/html/pt/index.html', {'request': request,})

def cursos(request):
    return render(request, 'UniversityConnect/html/pt/cursos.html', {'request': request,})