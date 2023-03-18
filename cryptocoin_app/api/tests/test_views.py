import pytest
from django.urls import reverse
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_unavtorised_request(auto_login_user):
    url = reverse('user-list')
    response = auto_login_user.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_post_viewset(auto_login_user, get_test_data):
    data = get_test_data
    url = reverse('cryptocurrencies-list')
    client = auto_login_user
    response = client.post(
        url, data=data, content_type='application/json')
    assert response.status_code == 201
    assert response.data['name'] == 'bobcoin'


@pytest.mark.django_db
def test_api_get_viewset(auto_login_user, get_test_data):
    data = get_test_data
    url = reverse('cryptocurrencies-list')
    client = auto_login_user
    client.post(
        url, data=data, content_type='application/json')

    response = client.get(url)
    assert response.status_code == 200
    assert response.data['results'][0]['symbol'] == 'BOBO'


@pytest.mark.django_db
def test_api_update_viewset(auto_login_user, get_test_data):
    data = get_test_data
    update_data = {'symbol': "BOBA"}
    url = reverse('cryptocurrencies-list')
    client = auto_login_user
    post_response = client.post(
        url, data=data, content_type='application/json')
    assert post_response.data['name'] == 'bobcoin'
    d = client.patch(f'{url}bobcoin/', data=update_data)
    print(d.data)
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['results'][0]['symbol'] == 'BOBA'


@pytest.mark.django_db
def test_api_delete_viewset(auto_login_user, get_test_data):
    data = get_test_data
    url = reverse('cryptocurrencies-list')
    client = auto_login_user
    post_response = client.post(
        url, data=data, content_type='application/json')
    assert post_response.data['name'] == 'bobcoin'
    delete_response = client.delete(f'{url}bobcoin/')
    assert delete_response.status_code == 204
