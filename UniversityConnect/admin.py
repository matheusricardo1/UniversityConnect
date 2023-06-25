from django.contrib import admin
from .models import Categoria, Formacao, NivelCurso, Curso

admin.site.register(Categoria)
admin.site.register(Formacao)
admin.site.register(NivelCurso)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'carga_horaria', 'mensalidade']
    list_filter = ['categoria', 'formacao', 'nivel_curso']
    search_fields = ['titulo', 'descricao']
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        # Verifica se o texto foi enviado pelo usuário
        novo_titulo = request.POST.get('novo_titulo')

        # Verifica se o primeiro curso existe
        primeiro_curso = Curso.objects.first()

        if novo_titulo and primeiro_curso:
            primeiro_curso.titulo = novo_titulo
            primeiro_curso.save()

        super().save_model(request, obj, form, change)