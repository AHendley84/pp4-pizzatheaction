from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import AddPostForm
from django.urls import reverse_lazy
from django.contrib import messages


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

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, 'Post added successfully!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:content_view', kwargs={'pk': self.object.pk})


class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'blog/update_post.html'
    fields = ['title', 'content',]

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)


class DeletePostView(DeleteView):
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:blog_home')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post deleted successfully!')
        return super().delete(request, *args, **kwargs)