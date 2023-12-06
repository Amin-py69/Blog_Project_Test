from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='detail'),
]
