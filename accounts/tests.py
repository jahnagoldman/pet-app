from django.contrib.auth import authenticate, login
from django.test import TestCase

# Create your tests here.
from accounts.forms import User


class LogInTest(TestCase):
    def setUp(self):
        self.credentials =  {
            'username': 'testuser',
            'password': 'testpassword',
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


