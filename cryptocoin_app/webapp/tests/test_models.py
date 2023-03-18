import pytest
from webapp.models import Cryptocurrency
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('John', '1f2f3h4h21')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_cryptocurrency_create():
    Cryptocurrency.objects.create(
        name='MyBestCoin',
        symbol='MBCN',
        price=1.0,
        percent_change_24h=1.0,
        percent_change_7d=1.0,
        volume_24h=1.0,
        circulating_supply=100)
    assert Cryptocurrency.objects.count() == 1
