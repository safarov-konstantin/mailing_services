from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Регистрация пользователей в админ панеле
    """
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name',)
