from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'created', 'is_published', 'image')
    list_display_links = None
    list_editable = ('is_published',)
    list_filter = ('category', 'title')
    search_fields = ('title', 'body')
    exclude = ('slug',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    pass
