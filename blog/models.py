from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=254)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # If the created_by field is not set, and there is a logged-in user,
        # set the created_by field to the current user.
        if not self.created_by and hasattr(self, 'request_user'):
            self.created_by = self.request_user
        super().save(*args, **kwargs)
