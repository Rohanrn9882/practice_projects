from django.db import models

# Create your models here.
class Laptop(models.Model):
    laptop_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    ram = models.CharField(max_length=30)
    rom = models.CharField(max_length=30)
    hdd = models.CharField(max_length=30)
    ssd = models.CharField(max_length=30)
    price = models.FloatField()