from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Brand, Category
from .forms import ProductForm

# Create your views here.
def all_products(request):
    """
    A view to show all products including sorting
    and search queries
    """

    products = Product.objects.all()
    query = None
    categories = None
    brands = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "No search parameters entered")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brands,
        'current_sorting': current_sorting,
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


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have access to this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'{product.name} added successfully')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(request, 'Product failed submission. Pleas review and ensure it is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have access to this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} edited successfully')
            return redirect(reverse('view_product', args=[product.id]))
        else:
            messages.error(request, f'{product.name} has not updated successfully. Please review and ensure it is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners have access to this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has been successfully deleted')
    return redirect(reverse('products'))
