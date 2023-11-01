from unittest import TestCase
from rest_framework.test import APIClient


class TestApi(TestCase):
    def test_sample(self):
        client = APIClient()
        url = '/test/'
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
