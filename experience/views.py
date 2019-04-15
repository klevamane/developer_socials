from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Experience
from .serializers import ExperienceSerializer


class CreateExperience(CreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class RetrieveUpdateExperience(RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
