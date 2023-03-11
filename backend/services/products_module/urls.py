from django.urls import path, include
from services.products_module.views import index

urlpatterns = [
    path('', index, name='index'),
]