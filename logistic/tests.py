import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def sample_test(self):
    client = APIClient()
    url = '/api/v1/stocks/'
    response = client.get(url)
    self.assertEqual(response.status_code, 200)
