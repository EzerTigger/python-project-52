from django.test import TestCase


class MainPageTest(TestCase):

    def test_main(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
