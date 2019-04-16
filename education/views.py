from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Education
from rest_framework.permissions import IsAuthenticated
from .serialzers import EducationSerializer


class ListCreateEducation(ListCreateAPIView):
    """Implements creating and listing objects for Education"""
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.education.all()

    def perform_create(self, serializer):
        serializer.save(developer=self.request.user)


class RetrieveUpdateDestroyEducation(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.education.all()
