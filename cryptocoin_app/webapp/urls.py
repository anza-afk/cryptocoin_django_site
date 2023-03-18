from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('users/register', views.register, name="register"),
    path('users/', include('django.contrib.auth.urls')),
    path('crypto/', views.CryptoView.as_view(), name='crypto'),
    path('detail', views.CryptoDetailView.as_view(), name='detail'),
    path('favorite', views.favorite_button, name='favorite'),
    path('refresh_data', views.refresh_data, name='refresh_data'),
]
