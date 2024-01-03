from django.db import models
from django.contrib.auth.models import User
from blog_app.manager import Article_Publish_Blog
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
    title = models.CharField(max_length=80, verbose_name='عنوان')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی')
    body = models.TextField(verbose_name='متن')
    image = models.ImageField(upload_to='image/article', verbose_name='عکس')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    is_published = models.BooleanField(default=True, verbose_name='عمومی شود')
    status = models.BooleanField(default=True, verbose_name='موقعیت')
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

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='relies')
    body = models.TextField(verbose_name='متن')
    created_add = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.body[:50]

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


class Message(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    email = models.EmailField(verbose_name='ایمیل')
    title = models.CharField(max_length=70, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'
