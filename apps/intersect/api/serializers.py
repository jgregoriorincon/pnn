from rest_framework import serializers
from apps.intersect.models import Intersect

class IntersectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intersect
        fields = '__all__'