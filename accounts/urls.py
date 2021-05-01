from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('accounts/sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('log-out/', views.Logout.as_view(), name='logout'),
]