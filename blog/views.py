from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import AddPostForm
from django.urls import reverse_lazy


class BlogHomeView(ListView):
    """
    A view to return all the blog entries
    """
    model = BlogPost
    template_name = 'blog/all_posts.html'
    context_object_name = 'all_objects'
    ordering = ['-created_on']


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


class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:blog_home')