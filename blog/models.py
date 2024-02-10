from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from datetime import datetime, date
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('BlogCategory', null=True, blank=False, on_delete=models.SET_NULL)
    #content = models.TextField()
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:content_view', args=[str(self.id)])

    def save(self, *args, **kwargs):
        # If the created_by field is not set, and there is a logged-in user,
        # set the created_by field to the current user.
        if not self.created_by and hasattr(self, 'request_user'):
            self.created_by = self.request_user
        super().save(*args, **kwargs)


class BlogCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name