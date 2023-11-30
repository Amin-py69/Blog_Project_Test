from django.shortcuts import render
from blog_app.models import Article


def home(request):
    article = Article.filter_manager.published()
    return render(request, 'home_app/index.html', {'articles': article})
