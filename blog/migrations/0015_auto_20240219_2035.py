# Generated by Django 3.2.23 on 2024-02-19 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_blogcomment_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='product_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='product_rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='purchase_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
