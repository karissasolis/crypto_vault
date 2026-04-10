from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='crypto_vault_app_home'),
]
