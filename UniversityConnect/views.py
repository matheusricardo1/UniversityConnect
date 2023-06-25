from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User, AnonymousUser
from googletrans import Translator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Curso


def homepage(request):
    user = request.user
    if isinstance(user, AnonymousUser):
        return render(request, 'UniversityConnect/html/pt/index.html', {
            'request': request,
            })
    else:
        social_account = user.socialaccount_set.first()
        if social_account:
            user_social = social_account.user
            return render(request, 'UniversityConnect/html/pt/index.html', {
            'request': request,
            'user': user_social,
            })
        else:
            return render(request, 'UniversityConnect/html/pt/index.html', {
            'request': request,
            })

    

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


@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'UniversityConnect/html/pt/profile.html')



