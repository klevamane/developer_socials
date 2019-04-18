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
    # params = {
    #     'firstname': 'test_dev1',
    #     'lastname': 'test_dev1',
    #     'email': 'test_dev1@test.com',
    #     'date_of_birth': '1992-01-01',
    #     'mobile': '08027538232',
    #     'password': 'password123'
    # }
    # print('got herererer')
    # # developer = Developer.create(**params)
    # developer = Developer(**params)
    # developer.save()
    serializer_class = DeveloperProfilesSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DeveloperProfilesSerializer(queryset, many=True)
        context = {
            'data': serializer.data,
            'message': 'successfully retrieved'
        }
        return Response(context, status=status.HTTP_200_OK)


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

