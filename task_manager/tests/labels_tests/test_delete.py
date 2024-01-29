from django.contrib.auth.models import User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.labels.models import Label


class DeleteLabel(TestCase):
    fixtures = ['db_label.json']

    def test_delete_open_without_login(self):
        response = self.client.get(reverse('delete_label', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_label(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('delete_label', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.client.post(
            reverse('delete_label', kwargs={'pk': 1})
        )
        statuses = Label.objects.all()
        self.assertEqual(len(statuses), 0)
