import os
import json
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)


class DeleteUserTest(TestCase):

    def test_delete(self):
        fixture = os.path.join(FIXTURE_DIR, 'user.json')
        test_user = json.load(open(fixture))
        username = test_user['username']
        password = test_user['password']
        user = User.objects.create_user(username=username, password=password)
        self.assertIn(user, User.objects.all())
        self.client.login(username=username, password=password)
        self.client.post(
            reverse_lazy(
                'delete',
                kwargs={'pk': user.id}
            )
        )
        self.assertNotIn(user, User.objects.all())

