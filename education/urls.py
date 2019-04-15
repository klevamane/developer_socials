from django.urls import path
from .views import ListCreateEducation, RetrieveUpdateDestroyEducation

urlpatterns = [
    path('', ListCreateEducation.as_view(), name='list_create_edu'),
    path('<int:pk>', RetrieveUpdateDestroyEducation.as_view(), name='retrieve_update_destroy_edu')
]
