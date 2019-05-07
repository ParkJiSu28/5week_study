from rest_framework.serializers import ModelSerializer
from .models import FilterPost

class FilterPostSerializer(ModelSerializer):
    class Meta:
        model=FilterPost
        fields = '__all__'