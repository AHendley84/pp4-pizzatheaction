# Generated by Django 3.2.23 on 2024-02-19 20:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20240219_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='product_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]