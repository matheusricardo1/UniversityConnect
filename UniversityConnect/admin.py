from django.contrib import admin
from .models import Categoria, Formacao, NivelCurso, Curso
from googletrans import Translator


def traduzir_titulo(modeladmin, request, queryset):
    translator = Translator(service_urls=['translate.google.com'])
    for curso in queryset:
        curso.tittle_en = translator.translate(curso.titulo, dest='en').text
        curso.mini_description_en = translator.translate(curso.mini_descricao, dest='en').text
        curso.description_en = translator.translate(curso.descricao, dest='en').text
        curso.save()
traduzir_titulo.short_description = 'Traduzir para inglês'


admin.site.register(Categoria)
admin.site.register(Formacao)
admin.site.register(NivelCurso)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    actions = [traduzir_titulo]
    list_display = ['titulo', 'carga_horaria', 'mensalidade']
    list_filter = ['categoria', 'formacao', 'nivel_curso']
    search_fields = ['titulo', 'descricao']
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        novo_titulo = request.POST.get('novo_titulo')
        primeiro_curso = Curso.objects.first()

        if novo_titulo and primeiro_curso:
            primeiro_curso.titulo = novo_titulo
            primeiro_curso.save()

        super().save_model(request, obj, form, change)



