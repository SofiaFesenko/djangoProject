from django.urls import path
from services.user_module.views import registration, auth

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('', auth, name='auth'),
]
