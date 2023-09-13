from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, default='English Name')
    

    def __str__(self):
        return self.name

class Education(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, default='English Name')

    def __str__(self):
        return self.name

class CourseLevel(models.Model):
    name = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100, default='English Name')

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    tittle_en = models.CharField(max_length=100, default='English Name')
    mini_description = models.TextField(max_length=255, default='English Description')
    mini_description_en = models.TextField(max_length=255, default='English Description')
    description = models.TextField(max_length=2000)
    description_en = models.TextField(max_length=2000, default='English Description')
    course_load = models.IntegerField()
    course_time = models.CharField(max_length=100)
    time_course_en = models.CharField(max_length=100, default='0 years')
    monthly_course_fee = models.DecimalField(max_digits=8, decimal_places=2)
    class_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cursos/cover/%Y/%m/%d/', blank=True, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    course_level = models.ForeignKey(CourseLevel, on_delete=models.CASCADE)
    link = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
