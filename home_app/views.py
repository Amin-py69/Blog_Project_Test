from django.shortcuts import render
from blog_app.models import Article


def home(request):
    article = Article.filter_manager.published()
    recent_article = Article.filter_manager.published().order_by('-created')[:3]
    return render(request, 'home_app/index.html', {'articles': article, 'recent_article': recent_article})
