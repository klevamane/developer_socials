import pytest
from rest_framework.test import APIClient
from django.urls import resolve, reverse


@pytest.mark.django_db
class TestDeveloperOperations:
    """Test the developer operations"""

    def test_developer_signup(self):
        signup_data = {
            'firstname': 'maples',
            'lastname': 'lehft',
            'email': 'mapples@test.com',
            'date_of_birth': '1992-01-01',
            'mobile': '08027538111',
            'password': 'password123'
        }
        path = reverse('list_create_dev')
        client = APIClient()
        response = client.post(path, signup_data)
        assert response.status_code == 201

    def test_list_all_developers(self, new_developer):
        path = reverse('list_create_dev')
        client = APIClient()
        response = client.get(path)
        assert response.status_code == 200
