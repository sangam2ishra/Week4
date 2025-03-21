from django.urls import path
from product import controllers

urlpatterns=[
    path('products/', controllers.get_all_products, name='get_all_products'),
    path('products/create/', controllers.create_product, name='create_product'),
    path('products/update/<str:product_id>/', controllers.update_product, name='update_product'),
    path('products/delete/<str:product_id>/', controllers.delete_product, name='delete_product'),
    path('products/<str:product_id>/', controllers.get_product, name='get_product'),
]