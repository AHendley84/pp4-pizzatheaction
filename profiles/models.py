from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaing default delivery
    information, order history and blog posts.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    default_phone_number = models.CharField(
            max_length=20, null=True, blank=True)
    default_address_line1 = models.CharField(
            max_length=80, null=True, blank=True)
    default_address_line2 = models.CharField(
            max_length=80, null=True, blank=True)
    default_town_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save UserProfile model first

        if (self.first_name or self.last_name) and (
            (self.first_name != self.user.first_name
                or self.last_name != self.user.last_name)
        ):
            if not self.user.first_name:
                self.user.first_name = self.first_name
            if not self.user.last_name:
                self.user.last_name = self.last_name
            self.user.save()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    else:
        instance.userprofile.save()
