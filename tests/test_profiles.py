from django.urls import resolve, reverse
from django.test import client, RequestFactory
from mixer.backend.django import mixer
from developer.views import ListDeveloperProfiles
from developer.serializers import DeveloperProfilesSerializer
from developer.models import Developer
import pytest
from rest_framework.test import APIClient
CHARSET = 'utf-8'


@pytest.mark.django_db
class TestProfiles:
    """Test the Developer URL"""

    # This tells django that your test needs database access

    def test_detail_url_path(self):
        # The reverse method gets the path by accepting the path name('retrieve_delete_update_dev')
        # and since the path expects an integer, we make use of the kwargs here
        path = reverse('retrieve_dev', kwargs={'pk': 1})
        # the resolve method is kind of the opposite of the reverse method
        assert resolve(path).view_name == 'retrieve_dev'

    # Sample:
    # def test_product_is_in_stock(self):
    #     product = Product.objects.create(
    #         ....
    #         ....
    #     )
    #     # instead of explicitly creating a sample product where we only want to edit a single attribute
    #     # we make use of mixer
    #     product = mixer.blend('app.Model', attribute_a=the_value)
    #     assert ...

    def test_get_list_of_all_developers(self, new_developer):
        new_developer.save()
        client = APIClient()
        path = reverse('list_devs')
        response = client.get(path)
        response_json = response.data['data']
        message = response.data['message']

        assert response.status_code == 200
        assert response_json[0]['id'] == new_developer.id
        assert response_json[0]['firstname'] == 'test_dev1'
        assert len(response_json) >= 1
        assert message == 'successfully retrieved'

    def test_get_details_of_a_single_developer(self, new_developer):
        new_developer.save()
        client = APIClient()
        path = reverse('retrieve_dev', kwargs={'pk': new_developer.id})
        response = client.get(path)
        response_json = response.data['data']
        assert response.status_code == 200

    # TODO: feature not yet implemented
    # def test_edit_details_of_a_developer(self, new_developer):
    #     new_developer.save()
    #     developer_id = new_developer.id
    #
    #     client = APIClient()
    #     path = reverse('retrieve_dev', kwargs={'pk': developer_id})
    #     update_data = {
    #         'twitter': 'http://twitter.com/test_user'
    #     }
    #     response = client.put(path, update_data)
    #     assert response.status_code == 200
