from django.db import models

# Create your models here.
class AiClass(models.Model):
    class_num = models.IntegerField()
    lecturer = models.CharField(max_length=30)
    students_name = models.CharField(max_length=30)
    students_num = models.IntegerField()


class Students(models.Model):
    class_num = models.IntegerField()
    name = models.CharField(max_length=30)
    phon_num = models.CharField(max_length=30)
    intro_text = models.TextField(max_length=300)