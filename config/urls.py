from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lsuopd/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('admin/defender/', include('defender.urls')),
    path('', include('core.urls', namespace='core')),
    path('', include('accounts.urls', namespace='account')),
    path('', include('customer.urls', namespace='customer')),
    path('', include('restaurant.urls', namespace='restaurant')),
    path('', include('contact.urls', namespace='contact')),
    path('accounts/', include('allauth.urls')),
]

handler404 = 'core.views.error_404'