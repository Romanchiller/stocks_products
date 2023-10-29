from unittest import TestCase

from rest_framework.test import APIClient


class TestSmth(TestCase):
    def sample_test(self):
        client = APIClient()
        url = '/api/v1/stocks/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
