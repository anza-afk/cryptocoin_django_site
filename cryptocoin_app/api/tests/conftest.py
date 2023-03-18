import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auto_login_user(db, api_client):
    user = User.objects.create(
       username='someone', password='password1'
    )
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def get_test_data(db):
    data = json.dumps({
        'name': "bobcoin",
        'symbol': "BOBO",
        'price': 2.1,
        'percent_change_24h': 2.1,
        'percent_change_7d': 2.1,
        'volume_24h': 2.1,
        'circulating_supply': 600,
        'favorite_by': []
    })
    return data
