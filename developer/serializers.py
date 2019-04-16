from rest_framework.serializers import ModelSerializer
from .models import Developer
from experience.serializers import ExperienceSerializer
from education.serialzers import EducationSerializer


class DeveloperSerializer(ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'
        read_only_fields = ('last_login', 'is_admin', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # calling the create user function in Developer Model
        # instead of implementing the normal implicit create we use the adhoc create method
        # the validated_data will contain all values passed from the request body, including required
        # and the optional passed, this will be received in the **extra_fields of create_user
        return Developer.objects.create_user(**validated_data)


class DeveloperProfilesSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
        read_only_fields = ('last_login', 'is_admin', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}


class SingleProfileSerializer(ModelSerializer):
    # The name 'experiences' is equivalent to the related_name
    experiences = ExperienceSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True)

    class Meta:
        model = Developer
        exclude = ['is_admin', 'is_active', 'password', 'date_of_birth', 'created_at', 'updated_at', 'last_login']
        read_only_fields = ('last_login', 'is_admin', 'is_active')
        extra_kwargs = {'password': {'write_only': True}}
