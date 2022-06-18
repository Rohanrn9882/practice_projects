from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    mark = models.FloatField()
    mail = models.EmailField()
    city = models.CharField(max_length=30)