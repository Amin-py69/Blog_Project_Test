from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# Create your views here.

def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog_app/post-details.html', {'article': article})


def post_list(request):
    articles = Article.filter_manager.published()
    return render(request, 'blog_app/post-list.html', {'articles': articles})


def category_details(request, pk=None):
    category = Category.objects.get(id=pk)
    articles = category.article_set.filter(is_published=True)
    return render(request, 'blog_app/post-list.html', {'articles': articles})