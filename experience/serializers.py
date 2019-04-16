from rest_framework.serializers import ModelSerializer
from .models import Experience


class ExperienceSerializer(ModelSerializer):
    """Implements the experience serializer"""

    class Meta:
        read_only_fields = ['developer']
        model = Experience
        fields = '__all__'