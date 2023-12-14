from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='detail'),
    path('list', views.post_list, name='list'),
    path('category/<int:pk>', views.category_details, name='category_detail'),
]
