from django.urls import path
from . import views

app_name = 'blog_app'
urlpatterns = [
    path('detail/<slug:slug>', views.post_detail, name='detail'),
    path('list', views.PostListView.as_view(), name='list'),
    path('category/<int:pk>', views.category_details, name='category_detail'),
    path('search', views.search, name='search_list'),
    path('contactus', views.contactus, name='contact_us')
]
