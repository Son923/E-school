from django.db import models

# Create your models here.
# class Profile(models.Models):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     bio = models.CharField(max_length=200, blank=True, null=True)
#     profile_pic = models.ImageField(default='default.png', upload_to = 'profile_pics')
#     is_teacher = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username + ' Profile'

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.profile_pic.path)
#         if img.height >100 or img.width>100:
#             output_size = (200,200)
#             img.thumbnail(output_size)
#             img.save(self.profile_pic.path)