from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from accounts.models import User
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
        'available',
    )
    list_filter = ('available',)
    search_fields = ('name', 'category')
    actions = ('make_available', 'make_unavailable')

    def make_available(self, request, queryset):
        updated = queryset.update(available=True)
        self.message_user(request, ngettext(
            '%d item was successfully marked as available.',
            '%d items were successfully marked as available.',
            updated,
        ) % updated, messages.SUCCESS)
    
    def make_unavailable(self, request, queryset):
        updated = queryset.update(available=False)
        self.message_user(request, ngettext(
            '%d this item was successfully marked as unavailable.',
            '%d this items were successfully marked as unavailable.',
            updated,
        ) % updated, messages.SUCCESS)


class OrderModelAdmin(admin.ModelAdmin):
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "user":
    #         kwargs["queryset"] = User.objects.filter(is_admin=True)
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

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