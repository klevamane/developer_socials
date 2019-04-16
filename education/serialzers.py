from rest_framework.serializers import ModelSerializer
from .models import Education


class EducationSerializer(ModelSerializer):
    class Meta:
        read_only_fields = ['developer']
        model = Education
        fields = '__all__'