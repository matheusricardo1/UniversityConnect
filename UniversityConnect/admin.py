from django.contrib import admin
from .models import Category, Education, CourseLevel, Course
from googletrans import Translator


def translate_course(modeladmin, request, queryset):
    translator = Translator(service_urls=['translate.google.com'])
    for course in queryset:
        course.tittle_en = (translator.translate(curso.title, dest='en').text).title()
        course.mini_description_en = translator.translate(course.mini_description, dest='en').text
        course.description_en = translator.translate(course.description, dest='en').text
        course.time_course_en = (translator.translate(course.course_time, dest='en').text).title()
        course.save()
translate_course.short_description = 'Traduzir para inglês'

def transalte_education(modeladmin, request, queryset):
    translator = Translator(service_urls=['translate.google.com'])
    for education in queryset:
        education.name_en = (translator.translate(education.name, dest='en').text).title()
        education.save()
transalte_education.short_description = 'Traduzir para inglês'

def translate_category(modeladmin, request, queryset):
    translator = Translator(service_urls=['translate.google.com'])
    for category in queryset:
        category.name_en = (translator.translate(category.name, dest='en').text).title()
        category.save()
translate_category.short_description = 'Traduzir para inglês'

def translate_course_level(modeladmin, request, queryset):
    translator = Translator(service_urls=['translate.google.com'])
    for course_level in queryset:
        course_level.name_en = (translator.translate(course_level.name, dest='en').text).title()
        course_level.save()
translate_course_level.short_description = 'Traduzir para inglês'

@admin.register(Education)
class FormacaoAdmin(admin.ModelAdmin):
    actions = [transalte_education]
    
@admin.register(Category)
class CategoriaAdmin(admin.ModelAdmin):
    actions = [translate_category]


@admin.register(CourseLevel)
class NivelCursoAdmin(admin.ModelAdmin):
    actions = [translate_course_level]


@admin.register(Course)
class CursoAdmin(admin.ModelAdmin):
    actions = [translate_course]
    list_display = ['title', 'course_load', 'monthly_course_fee']
    list_filter = ['category', 'education', 'course_level']
    search_fields = ['title', 'description']
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        novo_titulo = request.POST.get('novo_titulo')
        primeiro_curso = Course.objects.first()

        if novo_titulo and primeiro_curso:
            primeiro_curso.title = novo_titulo
            primeiro_curso.save()

        super().save_model(request, obj, form, change)



