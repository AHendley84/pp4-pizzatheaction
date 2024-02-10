from django.urls import path
from .views import BlogHomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView

app_name = 'blog'

urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog_home'),
    path('content/<int:pk>/', PostDetailView.as_view(), name='content_view'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('content/edit/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('content/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
]
