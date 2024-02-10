from django.contrib import admin
from .models import BlogPost, BlogCategory


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_by',
    )

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
