from django.contrib.auth.models import User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.labels.models import Label


class Create(TestCase):
    fixtures = ['db_label.json']

    def test_create_open_without_login(self):
        response = self.client.get(reverse('create_label'))
        self.assertEqual(response.status_code, 302)

    def test_create_label(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('create_label'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Label.objects.all().count(), 1)
        response = self.client.post(
            reverse('create_label'),
            {'name': 'test2'}
        )
        self.assertEqual(Label.objects.all().count(), 2)
