from django.shortcuts import render
from .models import Developer
from .serializers import DeveloperSerializer, DeveloperProfilesSerializer, SingleProfileSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView, RetrieveAPIView


class ListCreateDeveloper(ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class RetrieveUpdateDestroyDeveloper(RetrieveUpdateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DestroyDeveloper(DestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


# PROFILE SECTION
class ListDeveloperProfiles(ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperProfilesSerializer


class RetrieveDeveloperProfile(RetrieveAPIView):
    queryset = Developer.objects.all()
    serializer_class = SingleProfileSerializer

    def retrieve(self, request, *args, **kwargs):
        #  This returns details: 'Not found' implicitly
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        context = {
            'data': serializer.data,
            'success': True,
            'message': 'Operation Successful'
        }
        return Response(context, status=status.HTTP_200_OK)

