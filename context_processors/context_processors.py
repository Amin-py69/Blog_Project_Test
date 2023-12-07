from blog_app.models import Article


def recent_posts(request):
    recent_post = Article.filter_manager.published().order_by('-created')[:3]
    return {'recent_post': recent_post}