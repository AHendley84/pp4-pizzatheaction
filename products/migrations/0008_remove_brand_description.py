# Generated by Django 3.2.23 on 2024-02-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_brand_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='description',
        ),
    ]