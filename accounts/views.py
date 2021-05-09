from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.views import View
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .forms import (
    SignInForm,
    SignUpForm,
    UserProfileForm
)
from .models import User
from django.conf import settings
import requests


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
            data = form.cleaned_data
            remember = form.cleaned_data['remember']
            user = authenticate(email=data['email'], password=data['password'])
            response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': response
            }
            info = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            auth = info.json()
            if auth['success']:
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


class SignUp(View):
    template_name = 'account/sign_up.html'
    form_class = SignUpForm

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
            )
            user.is_active = False
            user.save()
            domain = get_current_site(request).domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            url = reverse('account:active-mail', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(user)})
            link = 'http://' + domain + url
            email = EmailMessage(
                'Activate your email address',
                link,
                'shayan.aimoradii@gmail.com',
                [data['email']]
            )
            email.send(fail_silently=False)
            messages.success(request, 'Please confirm your email address to complete the registration', 'success')
            return redirect('account:sign-in')
        return render(request, self.template_name, {'form': form})


class ActiveEmail(View):
    def get(self, request, uidb64, token):
        user_id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=user_id)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('account:sign-in')


class Logout(LoginRequiredMixin, View):
    login_url = 'account:sign-in'

    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out successfully', 'success')
        return redirect('/')


class PasswordReset(PasswordResetView):
    template_name = 'account/reset.html'
    success_url = reverse_lazy('account:done')
    email_template_name = 'account/link.html'


class PasswordDone(PasswordResetDoneView):
    template_name = 'account/done.html'


class PasswordConfirm(PasswordResetConfirmView):
    template_name = 'account/confirm.html'
    success_url = reverse_lazy('account:complete')


class PasswordComplete(PasswordResetCompleteView):
    template_name = 'account/complete.html'


class UserPanel(View):
    template_name = 'account/user_panel.html'

    def get(self, request):
        return render(request, self.template_name)


class UserProfile(UpdateView):
    template_name = 'account/profile.html'
    model = User
    form_class = UserProfileForm

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)


class ChangePassword(LoginRequiredMixin, View):
    template_name = 'account/change_pass.html'
    login_url = 'account:sign-in'
    form_class = PasswordChangeForm

    def get(self, request):
        form = self.form_class(request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!', 'success')
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Please correct the error below.', 'danger')
        return render(request, self.template_name, {'form': form})