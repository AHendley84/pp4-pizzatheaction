from django.urls import path
from .views import BlogHomeView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home'),
    path('content/<int:pk>/', BlogDetailView.as_view(), name='content_view'),
]
