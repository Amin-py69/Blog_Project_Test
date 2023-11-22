from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image/profile', blank=True, null=True)

    def __str__(self):
        return self.user.username
