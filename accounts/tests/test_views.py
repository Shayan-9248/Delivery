from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import (
    User,
    Profile
)
from accounts.forms import (
    SignInForm,
    SignUpForm
)

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_signup_GET(self):
        response = self.client.get(reverse('account:sign-up'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/sign_up.html')
        self.failUnless(response.context['form'], SignUpForm)
    
    def test_user_signup_POST_valid(self):
        response = self.client.post(reverse('account:sign-up'), data={
            'username': 'max',
            'email': 'max@email.com',
            'password': 'max123',
            'confirm_password': 'max123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)
    
    # def test_user_signup_POST_invalid(self):
    #     response = self.client.post(reverse('account:sign-up'), data={
    #         'username': 'max'
    #         'email': 'max.com',
    #         'password': '123',
    #         'confirm_password': '123'
    #     })
    #     self.assertEqual(response.status_code, 200)
    #     self.failIf(response.context['form'].is_valid())
    #     self.assertFormError(response, 'form', field='email', errors=['Please enter a valid email address'])