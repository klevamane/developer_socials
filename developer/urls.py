from django.contrib import admin
from django.urls import path
from .views import ListCreateDeveloper

urlpatterns = [
    path('', ListCreateDeveloper.as_view(), name='list_create_dev')
]