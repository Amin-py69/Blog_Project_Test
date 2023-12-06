from django.db import models
from django.contrib.auth.models import User
from blog_app.manager import Article_Publish_Blog
from django.utils.text import slugify
from django.urls import reverse


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
    is_published = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, default=' ')
    objects = models.Manager()
    filter_manager = Article_Publish_Blog()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
