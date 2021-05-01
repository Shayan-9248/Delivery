from django.shortcuts import render
from django.views import View
from .forms import (
    SignInForm
)


class SignIn(View):
    template_name = 'accounts/sign_in.html'
    form_class = SignInForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})