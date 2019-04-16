from django.contrib import admin
from django.urls import path
from .views import ListCreateDeveloper, ListDeveloperProfiles, RetrieveDeveloperProfile

urlpatterns = [
    path('', ListCreateDeveloper.as_view(), name='list_create_dev'),
    path('profiles/', ListDeveloperProfiles.as_view(), name='list_create_dev'),
    path('profiles/<int:pk>/', RetrieveDeveloperProfile.as_view(), name='retrieve_delete_update_dev')
]