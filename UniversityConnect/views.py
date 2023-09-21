from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.staticfiles import finders
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_protect
from .models import Category, Course, ExStudent, New, Places
from django.core.paginator import Paginator


def homepage(request):
    PAGE_NAME = 'UniversityConnect'
    user = request.user
    user_social = None
    if isinstance(user, AnonymousUser):
        return render(request, 'UniversityConnect/pages/index.html', {
            'request': request,
            'page_name':PAGE_NAME,
            })
    else:
        social_account = user.socialaccount_set.first()
        if social_account:
            user_social = social_account.user
            user_social.username = user_social.username.title()
            return render(request, 'UniversityConnect/pages/index.html', {
            'request': request,
            'user': user_social,
            'page_name':PAGE_NAME,
            })
        else:
            return render(request, 'UniversityConnect/pages/index.html', {
            'request': request,
            'page_name':PAGE_NAME,
            })
    return render(request, 'UniversityConnect/pages/index.html', {
            'request': request,
            'user': user_social,
            'page_name':PAGE_NAME,
            })

@csrf_protect
def courses(request):
    PAGE_NAME = 'Cursos'
    courses = Course.objects.all()
    
    category = Category.objects.all()
    
    paginator = Paginator(courses, 8)
    page_number = request.GET.get("page")
    courses = paginator.get_page(page_number)
    
    if 'en/' in request.path:
        lang = True
    else:
        lang = False 
    
    if request.GET.get('course-searchbar', ''):
        search_text = request.GET.get('course-searchbar', '')
        courses = courses.filter(
            Q(title__icontains=search_text) |
            Q(category_name__icontains=search_text) |
            Q(description__icontains=search_text)
        )
        context = {
            'request': request,
            'courses': courses,
            'search_text':search_text, 
            'page_name': PAGE_NAME,
            'category':category, 
            'lang':lang,
            }
        return render(request, 'UniversityConnect/pages/list.html', context=context)
    
    category_selected = request.GET.get('category', '')
    if category_selected != '':
        courses = Course.objects.filter(category=category_selected)
        paginator = Paginator(courses, 8)
        page_number = request.GET.get("page")
        courses = paginator.get_page(page_number)
    if len(courses) == 0:
        courses = False

    return render(request, 'UniversityConnect/pages/list.html', {
        'request': request, 
        'courses': courses,
        'page_name': PAGE_NAME,
        'category':category,
        'lang':lang,
        })



def courses_detail(request, id):
    course = get_object_or_404(Course,id=id,)
    other_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:2]

    lang = False 
    if 'en/' in request.path:
        lang = True
        

    PAGE_NAME = f'{course.title}'
    context = {
        'request': request,
        'course': course,
        'other_courses': other_courses, 
        'page_name': PAGE_NAME,
        'lang': lang, 
        'monthly_course_fee': course.monthly_course_fee/4,}
    return render(request, 'UniversityConnect/pages/courses_detail.html', context=context)


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    PAGE_NAME = f'Perfil - {user.first_name.title()}'
    if user.is_authenticated and SocialAccount.objects.filter(user=user, provider='google').exists():
        google_account = SocialAccount.objects.get(user=user, provider='google')
        email = google_account.extra_data['email']
    else:
        email = "Email não cadastradado!"

    context = {
        'request': request,
        'page_name': PAGE_NAME,
        'user':user, 
        'email':email,}

    return render(request, 'UniversityConnect/pages/profile.html', context=context)



def history(request):
    new = New.objects.first()

    return render(request, 'UniversityConnect/pages/history.html', {
        'page_name': 'História de Cambridge',
        'new': new,
    })

def ex_students(request):
    students = ExStudent.objects.all()
    paginator = Paginator(students, 6)
    page_number = request.GET.get("page")
    students = paginator.get_page(page_number)
    return render(request, 'UniversityConnect/pages/list.html', {
        'page_name': 'História de Cambridge',
        'students': students,
    })
    
    
def places(request):
    all_places = Places.objects.all()
    paginator = Paginator(all_places, 5)
    page_number = request.GET.get("page")
    paginated_places = paginator.get_page(page_number)
    return render(request, 'UniversityConnect/pages/list.html', {
        'page_name': 'Moradias',
        'places': paginated_places,
    })
    
    
    
def about(request):
    return render(request, 'UniversityConnect/pages/team.html', {
        'page_name': 'Quem somos',
    })
    