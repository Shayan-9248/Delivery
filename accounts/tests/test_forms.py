from django.test import TestCase
from accounts.forms import (
    SignInForm,
    SignUpForm
)

class TestSignUpForm(TestCase):
    def test_valid_data(self):
        form = SignUpForm(data={
            'username': 'kevin',
            'email': 'kevin@email.com',
            'password': 'kevin123',
            'confirm_password': 'kevin123'
        })
        self.assertTrue(form.is_valid())
    
    def test_invalid_data(self):
        form = SignInForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)


class TestSignInForm(TestCase):
    def test_valid_data(self):
        form = SignInForm(data={
            'email': 'kevin@email.com',
            'password': 'kevin123',
            'remember': True,
            'captcha': 'IDGS'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)