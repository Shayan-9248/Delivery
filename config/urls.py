from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls', namespace='account')),
    path('', include('customer.urls', namespace='customer')),
    path('', include('restaurant.urls', namespace='restaurant')),
    path('captcha/', include('captcha.urls')),
]
