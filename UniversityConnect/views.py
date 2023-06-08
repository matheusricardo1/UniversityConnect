from django.shortcuts import render

def homepage(request):
    return render(request, 'UniversityConnect/html/index.html')