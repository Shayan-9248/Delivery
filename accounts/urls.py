from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('accounts/sign-in/', views.SignIn.as_view(), name='sign-in'),
    path('accounts/sign-up/', views.SignUp.as_view(), name='sign-up'),
    path('active-mail/<uidb64>/<token>/', views.ActiveEmail.as_view(), name='active-mail'),
    path('log-out/', views.Logout.as_view(), name='logout'),
    path('reset-password/', views.PasswordReset.as_view(), name='reset'),
    path('password-done/', views.PasswordDone.as_view(), name='done'),
    path('confirm-password/<uidb64>/<token>/', views.PasswordConfirm.as_view(), name='confirm'),
    path('complete-password-reset/', views.PasswordComplete.as_view(), name='complete'),
]