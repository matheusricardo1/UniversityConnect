from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, default='English Name')
    

    def __str__(self):
        return self.nome

class Formacao(models.Model):
    nome = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, default='English Name')

    def __str__(self):
        return self.nome

class NivelCurso(models.Model):
    nome = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, default='English Name')

    def __str__(self):
        return self.nome

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    tittle_en = models.CharField(max_length=100, default='English Name')
    mini_descricao = models.TextField(max_length=255, default='English Description')
    mini_description_en = models.TextField(max_length=255, default='English Description')
    descricao = models.TextField(max_length=2000)
    description_en = models.TextField(max_length=2000, default='English Description')
    carga_horaria = models.IntegerField()
    tempo_curso = models.CharField(max_length=100)
    time_course_en = models.CharField(max_length=100, default='0 years')
    mensalidade = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_aula = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cursos/cover/%Y/%m/%d/', blank=True, default="")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    formacao = models.ForeignKey(Formacao, on_delete=models.CASCADE)
    nivel_curso = models.ForeignKey(NivelCurso, on_delete=models.CASCADE)
    botao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
