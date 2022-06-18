from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['cid', 'fname', 'lname', 'mail', 'city', 'mob_no', 'product', 'price', 'image']

admin.site.register(Customer, CustomerAdmin)
