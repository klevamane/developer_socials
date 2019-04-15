from django.contrib import admin
from django.urls import path
from .views import RetrieveUpdateExperience, CreateExperience

urlpatterns = [
    path('<int:pk>', RetrieveUpdateExperience.as_view(), name="retrieve_update_destroy_exp"),
    path('', CreateExperience.as_view(), name="create_exp")
]
