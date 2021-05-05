from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts import views


class TestUrls(SimpleTestCase):
    def test_sign_in(self):
        url = reverse('account:sign-in')
        self.assertEqual(resolve(url).func.view_class, views.SignIn)
    
    def test_sign_up(self):
        url = reverse('account:sign-up')
        self.assertEqual(resolve(url).func.view_class, views.SignUp)

    def test_log_out(self):
        url = reverse('account:logout')
        self.assertEqual(resolve(url).func.view_class, views.Logout)
    
    def test_active_email(self):
        url = reverse('account:active-mail', args=['uidb64', 'token'])
        self.assertEqual(resolve(url).func.view_class, views.ActiveEmail)
    
    def test_password_reset(self):
        url = reverse('account:reset')
        self.assertEqual(resolve(url).func.view_class, views.PasswordReset)
    
    def test_password_done(self):
        url = reverse('account:done')
        self.assertEqual(resolve(url).func.view_class, views.PasswordDone)

    def test_password_confirm(self):
        url = reverse('account:confirm', args=['uidb46', 'token'])
        self.assertEqual(resolve(url).func.view_class, views.PasswordConfirm)

    def test_password_complete(self):
        url = reverse('account:complete')
        self.assertEqual(resolve(url).func.view_class, views.PasswordComplete)