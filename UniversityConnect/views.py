from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from googletrans import Translator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Curso
#from models 

def homepage(request):
    return render(request, 'UniversityConnect/html/pt/index.html', {'request': request,})

@csrf_protect
def cursos(request):
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


def entrar(request):
    if request.method == 'GET':
        return render(request, 'UniversityConnect/html/pt/entrar.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) 
        if user:
            login(request, user)
            auth_text = f"User Logou!{user.username}"
        else:
            auth_text = "User não conseguir entrar!"
        
        return render(request, 'UniversityConnect/html/pt/cadastrar.html', {'auth': auth_text,})

@login_required(login_url='/entrar/')
def plataforma(request):
    curso = Curso.objects.all()
    auth_text = "Você fez login"
    return render(request, 'UniversityConnect/html/pt/entrar.html', {
        'auth': auth_text,
        'request': request,
        'curso': curso, 
    })

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'UniversityConnect/html/pt/cadastrar.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        user_email = User.objects.filter(email=email).first()
        if user or user_email:
            auth_text = "username ou email já cadastrados!"
            return render(request, 'UniversityConnect/html/pt/cadastrar.html', {'auth': auth_text,})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        auth_text = "User created"
        return render(request, 'UniversityConnect/html/pt/cadastrar.html', {'auth': auth_text,})

