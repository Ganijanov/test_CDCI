from django.test import TestCase
from django.urls import reverse

class CoreViewsTest(TestCase):
    def test_index_page(self):
        # Проверяем, что страница / работает
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, CI/CD!")
        