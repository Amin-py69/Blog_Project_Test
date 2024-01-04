from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import Article, Category, Comment, Message, Like
from .forms import ContactUs, MessageForm
from django.views.generic.list import ListView
# from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoadLogin
from django.views.generic.detail import DetailView
from django_ajax.decorators import ajax
from django.contrib.auth.decorators import login_required


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


class PostListView(LoadLogin, ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 1
    template_name = 'blog_app/post-list.html'
    queryset = Article.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Article
    template_name = 'blog_app/post-details.html'


@login_required
def like(request, slug, pk):
    if request.method == 'POST':
        if request.user.like(article_id=pk, article__slug=slug).exists():
            likes = Like.objects.get(user_id=request.user.id, article__slug=slug)
            likes.delete()
        else:
            Like.objects.create(article_id=pk, user_id=request.user.id)
