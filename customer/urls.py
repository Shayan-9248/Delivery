from django.urls import path
from . import views

app_name = 'customer'


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('order/', views.Order.as_view(), name='order'),
    path('request/<price>/<int:order_id>/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
]