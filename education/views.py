from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Education
from .serialzers import EducationSerializer


class ListCreateEducation(ListCreateAPIView):
    """Implements creating and listing objects for Education"""
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class RetrieveUpdateDestroyEducation(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
