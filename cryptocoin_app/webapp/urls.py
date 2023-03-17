from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/register', views.register, name="register"),
    path('users/', include('django.contrib.auth.urls'))
]