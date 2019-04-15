from django.shortcuts import render
from .models import Developer
from .serializers import DeveloperSerializer

# Create your views here.
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView


class ListCreateDeveloper(ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class RetrieveUpdateDestroyDeveloper(RetrieveUpdateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DestroyDeveloper(DestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
