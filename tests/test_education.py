import pytest
from django.urls import reverse, resolve
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestDeveloperEducation:
    """Implements tests to add =, delete and update a developer education"""
    client = APIClient()
    edu_path = reverse('list_create_edu')
    login_details = {
        'email': '',
        'password': 'password123',
    }
    context = {
        'institution_name': 'University of Port-Harcourt',
        'developer': '',
        '_from': '2015-01-10',
        'degree': 'B.Eng Software Engineering',
        'location': 'Port-Harcourt'

    }
    login_path = reverse('token_obtain_pair')

    def test_add_developer_education_succeeds(self, new_developer):
        """
        This method implements the test to add developer education
        :param new_developer: A fixture to create a new developer (user)
        :return: null
        """
        new_developer.save()

        self.login_details['email'] = new_developer.email

        response = self.client.post(self.login_path, self.login_details, format='json')
        token = response.data
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token['access'])
        assert response.status_code == 200

        self.context['developer'] = new_developer.id
        edu_response = self.client.post(self.edu_path, self.context)
        assert edu_response.status_code == 201

    def test_add_developer_education_with_incomplete_details_fails(self, new_developer):
        """
        This method implements the test to add developer education with in complete details
        it also make use of forced authentication
        :param new_developer: A fixture to create a new developer (user)
        :return: null
        """
        new_developer.save()
        self.client.force_authenticate(user=new_developer)
        self.context['location'] = ''
        edu_response = self.client.post(self.edu_path, self.context)
        response_data = edu_response.data
        assert edu_response.status_code == 400
        assert 'location' in response_data
