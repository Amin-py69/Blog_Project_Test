from blog_app.models import Article, Category


def recent_posts(request):
    recent_post = Article.filter_manager.published().order_by('-created')[:3]
    return {'recent_post': recent_post}


def recent_category(request):
    categories = Category.objects.all()
    return {'categories': categories}