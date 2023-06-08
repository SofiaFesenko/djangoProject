from django.urls import path
from services.user_module.views import reservation

urlpatterns = [
    path('', reservation, name='reservation'),
]
