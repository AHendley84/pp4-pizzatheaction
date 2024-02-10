from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from datetime import datetime, date

from .models import BlogPost, BlogCategory
from .forms import AddPostForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(BlogPost, id=self.kwargs['pk'])
        total_likes = post.total_likes()

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


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
    fields = ['title', 'content','category',]

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


def LikeView(request, pk):
    post = get_object_or_404(BlogPost, id=request.POST.get('post_like'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('blog:content_view', args=[str(pk)]))