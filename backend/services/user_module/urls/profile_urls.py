from django.urls import path
from services.user_module.views import profile

urlpatterns = [
    path('', profile, name='profile'),
]
