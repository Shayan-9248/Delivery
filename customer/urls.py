from django.urls import path
from . import views

app_name = 'customer'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('order/', views.Order.as_view(), name='order'),
]