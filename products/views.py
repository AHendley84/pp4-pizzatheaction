from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Brand, Category

# Create your views here.
def all_products(request):
    """
    A view to show all products including sorting
    and search queries
    """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "No search parameters entered")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    
    return render(request, 'products/products.html', context)


def view_product(request, product_id):
    """
    A view to show all the details of a single product.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/view_product.html', context)


def view_all_brands(request):
    """
    A view to show all the brands.
    """

    brands = Brand.objects.all()

    context = {
        'brands': brands,
    }
    
    return render(request, 'products/view_all_brands.html', context)


def view_all_categories(request):
    """
    A view to show all the categories.
    """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    
    return render(request, 'products/view_all_categories.html', context)