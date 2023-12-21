from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment, Message
from .forms import ContactUs, MessageForm


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


def search(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        articles = Article.objects.filter(title__icontains=q)
        page_number = request.GET.get('page')
        paginator = Paginator(articles, 1)
        page_list = paginator.get_page(page_number)
        return render(request, 'blog_app/post-list.html', {'articles': page_list})


def contactus(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            title = form.cleaned_data.get('title')
            text = form.cleaned_data.get('text')
            Message.objects.create(name=name, email=email, title=title, text=text)

        # instance = form.save(commit=False)
        # instance.name = 'ali'
        # instance.save()

    else:
        form = MessageForm()
    return render(request, 'blog_app/contact-us.html', {'form': form})
