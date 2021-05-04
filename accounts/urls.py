from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('accounts/sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('accounts/sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('active-mail/<uidb64>/<token>/', views.ActiveEmail.as_view(), name='active-mail'),
    path('log-out/', views.Logout.as_view(), name='logout'),
]