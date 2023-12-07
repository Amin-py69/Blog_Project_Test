from django.shortcuts import render
from .models import Article


# Create your views here.

def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'blog_app/post-details.html', {'article': article})


def post_list(request):
    articles = Article.filter_manager.published()
    return render(request, 'blog_app/post-list.html', {'articles': articles})
