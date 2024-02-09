import json
import os
from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)


class CreateUserTest(TestCase):

    def test_open_create_page(self):
        response = self.client.get(reverse_lazy('create_user'))
        self.assertEqual(response.status_code, 200)

    def test_create_user_and_redirect(self):
        fixture = os.path.join(FIXTURE_DIR, 'user.json')
        test_user = json.load(open(fixture))
        response = self.client.post(
            reverse_lazy('create_user'),
            test_user
        )
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, test_user.get('username'))
        self.assertRedirects(response, reverse_lazy('login'))
