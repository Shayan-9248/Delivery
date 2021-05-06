from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('lsuopd/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('admin/defender/', include('defender.urls')),
    path('', include('core.urls', namespace='core')),
    path('', include('accounts.urls', namespace='account')),
    path('', include('customer.urls', namespace='customer')),
    path('', include('restaurant.urls', namespace='restaurant')),
    path('', include('contact.urls', namespace='contact')),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('allauth.urls')),
]
