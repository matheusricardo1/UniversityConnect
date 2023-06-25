from django.shortcuts import render
from .models import Curso
#from models 

def homepage(request):
    return render(request, 'UniversityConnect/html/pt/index.html', {'request': request,})

def cursos(request):
    curso = Curso.objects.all()
    return render(request, 'UniversityConnect/html/pt/cursos.html', {
        'request': request,
        'curso': curso, 
    })

def atualizar_titulo(request):
    if request.method == 'POST':
        novo_titulo = request.POST.get('novo_titulo')
        primeiro_curso = Curso.objects.first()

        if novo_titulo and primeiro_curso:
            primeiro_curso.titulo = novo_titulo
            primeiro_curso.save()

    curso = Curso.objects.all()
    return render(request, 'UniversityConnect/html/pt/cursos.html', {
        'request': request,
        'curso': curso, 
    })