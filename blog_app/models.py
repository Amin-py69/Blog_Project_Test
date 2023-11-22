from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Article(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    category = models.ManyToManyField(Category)
    body = models.TextField()
    image = models.ImageField(upload_to='image/article')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
