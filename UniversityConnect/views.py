from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from googletrans import Translator
from .models import Curso
#from models 

def homepage(request):
    return render(request, 'UniversityConnect/html/pt/index.html', {'request': request,})

@csrf_protect
def cursos(request):
    curso = Curso.objects.all()
    return render(request, 'UniversityConnect/html/pt/cursos.html', {
        'request': request,
        'curso': curso, 
    })


@csrf_protect
def atualizar_titulo(request):
    if request.method == 'POST':
        novo_titulo = request.POST.get('novo_titulo')
        primeiro_curso = Curso.objects.first()

        if novo_titulo and primeiro_curso:
            primeiro_curso.titulo = novo_titulo
            trans = Translator()
            novo_titulo_en = trans.translate(novo_titulo, dest='en').text
            
            primeiro_curso.tittle_en = novo_titulo_en
            primeiro_curso.save()

    curso = Curso.objects.all()
    return render(request, 'UniversityConnect/html/pt/cursos.html', {
        'request': request,
        'curso': curso, 
    })