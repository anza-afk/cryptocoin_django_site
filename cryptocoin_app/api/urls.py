from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(
    r'cryptocurrencies',
    views.CryptocurrencyViewSet,
    basename="cryptocurrencies"
)
router.register(
    r'users',
    views.UserViewSet,
    basename="user"
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    ))
]
