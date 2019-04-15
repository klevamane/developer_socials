from rest_framework.serializers import ModelSerializer
from .models import Developer


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
