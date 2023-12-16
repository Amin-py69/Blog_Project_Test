from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment


# Create your views here.

def post_detail(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, parent_id=parent_id, user=request.user)
    return render(request, 'blog_app/post-details.html', {'article': article})


def post_list(request):
    articles = Article.filter_manager.published()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    page_list = paginator.get_page(page_number)
    return render(request, 'blog_app/post-list.html', {'articles': page_list})


def category_details(request, pk=None):
    category = Category.objects.get(id=pk)
    articles = category.article_set.filter(is_published=True)
    return render(request, 'blog_app/post-list.html', {'articles': articles})