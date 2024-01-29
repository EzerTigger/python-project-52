from django.contrib.auth.models import User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.labels.models import Label


class UpdateStatus(TestCase):
    fixtures = ['db_label.json']

    def test_update_open_without_login(self):
        response = self.client.get(reverse('update_label', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_update_mark(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('update_label', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.client.post(
            reverse('update_label', kwargs={'pk': 1}),
            {'name': 'test2'}
        )
        label = Label.objects.get(pk=1)
        self.assertEqual(label.name, 'test2')
