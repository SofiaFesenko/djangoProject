from django.urls import path

from .user_module import views as user_views

urlpatterns = [
    path('', user_views.index, name='index'),
]