import os
import json
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy


FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)
FIXTURE_FILE = os.path.join(FIXTURE_DIR, 'user.json')
TEST_USER = json.load(open(FIXTURE_FILE))


class UpdateUserTest(TestCase):
    fixtures = ['db.json']

    def test_update(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        self.client.post(
            reverse_lazy(
                'update',
                kwargs={'pk': user.id}
            ),
            TEST_USER
        )
        updated_user = User.objects.get(pk=user.id)
        self.assertEqual(updated_user.first_name, TEST_USER.get('first_name'))
        self.assertEqual(updated_user.last_name, TEST_USER.get('last_name'))
        self.assertEqual(updated_user.username, TEST_USER.get('username'))
