from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    image = models.ImageField(upload_to='image/article')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
