from django.shortcuts import render


def blog_home(request):
    """
    A view to retun the blog page
    """
    return render(request, 'blog/blog.html')