from django.contrib import admin
from .models import (
    Category,
    MenuItem,
    OrderModel,
)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'price', 
        'category', 
        'image_thumbnail',
    )
    search_fields = ('name', 'category')


class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone',
        'created',
        'is_paid',
        'is_shipped'
    )
    list_filter = ('is_paid', 'is_shipped')
    search_fields = ('name', 'email')


admin.site.register(Category)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(OrderModel, OrderModelAdmin)