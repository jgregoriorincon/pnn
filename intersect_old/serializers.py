from rest_framework import serializers
from intersect.models import Intersect

class IntersectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intersect
        fields = ('codigo_departamento', 'nombre_departamento', 'id_area', 'nombre_area', 'area_ha')