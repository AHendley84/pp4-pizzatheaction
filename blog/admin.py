from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_by',
    )

admin.site.register(BlogPost)
