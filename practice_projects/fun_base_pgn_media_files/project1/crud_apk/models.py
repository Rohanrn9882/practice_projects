from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    mail = models.EmailField()
    city = models.CharField(max_length=30)
    mob_no = models.IntegerField()
    product = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
