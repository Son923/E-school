from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    is_student = models.BooleanField()
    is_teacher = models.BooleanField(default=False)
    full_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username + ' Profile'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        full_name = f"{instance.first_name} {instance.last_name}"
        Profile.objects.create(user=instance, full_name=full_name)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()