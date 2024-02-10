from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogPost
from .forms import AddPostForm


class BlogHomeView(ListView):
    """
    A view to return all the blog entries
    """
    model = BlogPost
    template_name = 'blog/all_posts.html'
    context_object_name = 'all_objects'


class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_details.html'


class AddPostView(CreateView):
    model = BlogPost
    form_class = AddPostForm
    template_name = 'blog/add_post.html'

class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'blog/update_post.html'
    fields = ['title', 'content',]