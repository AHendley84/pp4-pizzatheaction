from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.view_product, name='view_product'),
    path('brands/', views.view_all_brands, name='view_all_brands'),
    path('categories/', views.view_all_categories, name='view_all_categories'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
