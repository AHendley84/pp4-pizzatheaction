from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogPost


class BlogHomeView(ListView):
    """
    A view to return all the blog entries
    """
    model = BlogPost
    template_name = 'blog/all_blogs.html'
    context_object_name = 'all_objects'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_details.html'


class AddPostView(CreateView):
    model = BlogPost
    template_name = 'blog/add_post.html'
    fields = [
        'title',
        'created_by',
        'content',
    ]
