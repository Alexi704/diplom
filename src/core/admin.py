from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Вывод отображаемых полей в админке, в разделе "Пользователи":
    list_display = ('username', 'email', 'first_name', 'last_name')
    # Организуем поиск, по заданным полям:
    search_fields = ('email', 'first_name', 'last_name', 'username')
    # Ставим фильтры (для сортировки пользователей):
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    # Выставляем поля админки в нужном нам порядке
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name',
                                      'email',)},),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',)},),
        ('Important dates', {'fields': ('last_login',
                                        'date_joined',)},),)
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name',
                                      'last_name',
                                      'email',)},),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',)},),
    )

    # Делаем поля неизменными(только для чтения):
    readonly_fields = ('last_login', 'date_joined')

    # Полностью скрываем поля в админке
    # exclude = ('password',)


# Меняем заголовок админки
admin.site.site_title = 'Панель администратора «TodoList»'
admin.site.site_header = 'Todo LIST: Администрирование'
