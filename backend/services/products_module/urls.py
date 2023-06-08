from django.urls import path, include

from services.products_module import views
from services.products_module.views import index, get_my_products, get_product, create_product, update_product, \
    delete_product

urlpatterns = [
    path('', index, name='index'),
    path('my_products/', get_my_products, name='my_products'),
    path('product/<int:pk>', get_product, name='product'),
    path('product/update/<int:pk>', update_product, name='product_update'),
    path('product/delete/<int:pk>', delete_product, name='product_delete'),
    path('product/create_product', create_product, name='create_product'),
    path('category/<str:category>', views.CategoryProducts.as_view(), name='category'),
]
