from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .forms import (
    SignInForm
)


class SignIn(View):
    template_name = 'account/sign_in.html'
    form_class = SignInForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        next = request.GET.get('next')
        form = self.form_class(request.POST)
        if form.is_valid():
            human = True
            data = form.cleaned_data
            remember = form.cleaned_data['remember']
            user = authenticate(email=data['email'], password=data['password'])
            if user is not None:
                if next:
                    return redirect(next)
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)
                else:
                    request.session.set_expiry(86400)
                return redirect('/')
            else:
                form.add_error('email', 'email or password is incorrect')
        else:
            messages.error(request, 'Invalid Recaptcha', 'danger')
        return render(request, self.template_name, {'form': form})


class Logout(LoginRequiredMixin, View):
    login_url = 'account:sign-in'

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('/')