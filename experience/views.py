from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Experience
from .serializers import ExperienceSerializer


class CreateExperience(ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (IsAuthenticated,)

    # we can make this in a def post function
    def perform_create(self, serializer):
        # updating the developer attribute in the model class
        # we may also decide to check if something already exist before creating in order to add a custom message
        # if we want
        serializer.save(developer=self.request.user)

    def get_queryset(self):
        """Get all experiences associated with the currently logged in (Token-ed) user"""
        return self.request.user.experiences.all()


class RetrieveUpdateExperience(RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):

        # return details: not found if not found
        object_instance = self.get_object()

        serializer = self.get_serializer(object_instance)

        if serializer.data['developer'] != request.user.id:
            context = {'message': 'The developer experience was not found'}
            return Response(context, status=status.HTTP_404_NOT_FOUND)

        context = {
            'data': serializer.data,
            'message': 'successfully retrieved'
        }
        return Response(context, status=status.HTTP_200_OK)

    # This another way of doing almost the same thing but no way to get granular to change the message
    # def get_queryset(self):
        # this is making use of the related_name in the model class
        # developer_experiences = self.request.user.experiences.all()
        # return developer_experiences
        # return context

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if serializer.data['developer'] != request.user.id:
            context = {'message': 'The developer experience was not found'}
            return Response(context, status=status.HTTP_404_NOT_FOUND)
        self.perform_destroy(instance)
        context = {'message': 'The user experience has been successfully deleted'}
        return Response(context, status=status.HTTP_200_OK)
