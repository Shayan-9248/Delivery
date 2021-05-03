from django.urls import path
from . import views

app_name = 'restaurant'


urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('order-detail/<int:id>/', views.OrderDetail.as_view(), name='detail'),
]