from django.urls import path
from .views import BlogHomeView, BlogDetailView, AddPostView

app_name = 'blog'

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home'),
    path('content/<int:pk>/', BlogDetailView.as_view(), name='content_view'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
