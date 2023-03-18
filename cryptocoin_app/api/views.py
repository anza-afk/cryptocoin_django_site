from rest_framework import permissions, viewsets

from django.contrib.auth.models import User
from webapp.models import Cryptocurrency
from .serializers import UserSerializer, CryptocurrencySerializer
from .mixins import MultipleFieldLookupMixin


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that returns list of all users
    and allow to rettiewe single user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CryptocurrencyViewSet(MultipleFieldLookupMixin, viewsets.ModelViewSet):
    """
    API endpoint that returns list of all cryptocurrencies,
    allow to retrieve single cryptocurrency by symbol,
    allows cryptocurrency to be viewed, edited or deleted.
    """
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    lookup_fields = ('symbol', 'name')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
