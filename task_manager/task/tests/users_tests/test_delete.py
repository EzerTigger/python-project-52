from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class DeleteUserTest(TestCase):

    def test_delete(self):
        user = User.objects.create_user(username='Vasya', password='qwerty')
        self.assertIn(user, User.objects.all())
        self.client.login(username='Vasya', password='qwerty')
        self.client.post(
            reverse_lazy(
                'delete',
                kwargs={'pk': user.id}
            )
        )
        self.assertNotIn(user, User.objects.all())

