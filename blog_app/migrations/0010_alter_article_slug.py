# Generated by Django 4.2.7 on 2023-12-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, default=' '),
        ),
    ]
