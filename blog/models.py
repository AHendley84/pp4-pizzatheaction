from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('BlogCategory', null=True, blank=False, on_delete=models.SET_NULL)
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    comments = models.ManyToManyField('BlogComment', related_name='post_comments', blank=True)

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

        # Update updated_on only when there are actual changes
        if self.pk is not None:
            original = BlogPost.objects.get(pk=self.pk)
            if original.title != self.title or original.content != self.content:
                self.updated_on = timezone.now()

        super().save(*args, **kwargs)


class BlogCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="post_comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    comments = models.TextField()
    comment_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)