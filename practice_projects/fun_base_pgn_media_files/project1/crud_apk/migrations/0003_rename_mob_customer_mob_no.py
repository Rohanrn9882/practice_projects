# Generated by Django 4.0.4 on 2022-06-11 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_apk', '0002_customer_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mob',
            new_name='mob_no',
        ),
    ]