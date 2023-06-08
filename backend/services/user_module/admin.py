from django.contrib import admin
from django.contrib.auth import get_user_model

from services.user_module.models import UserAddress

User = get_user_model()


class UserAddressInline(admin.TabularInline):
    model = UserAddress


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    search_fields = ['id', 'first_name', 'last_name', 'email']
    inlines = [UserAddressInline]
