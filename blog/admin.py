from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogComment


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
admin.site.register(BlogComment)
