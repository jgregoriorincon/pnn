from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import IntersectSerializer
from .models import Intersect

# Create your views here.
@api_view(['GET'])
def ShowAll(request):
    resultadosIntersect = Intersect.objects.raw('''SELECT B.id_resguardo, B.nombre_resguardo_indigena, A.nombre_departamento,  
                                                        round(ST_Area(ST_Transform(ST_Intersection(A.shape, B.shape), 3116))::numeric, 2) AS Area_Intersect_Ha
                                                    FROM public.departamentos A, public.resguardo B
                                                    WHERE ST_Intersects(A.shape, B.shape)
                                                    ORDER BY B.id_resguardo, A.codigo_departamento''')
    serializer = resultadosIntersect(resultadosIntersect, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowDpto(request, coddane):
    resultadosIntersect = Intersect.objects.raw('''SELECT B.id_resguardo, B.nombre_resguardo_indigena, A.nombre_departamento,  
                                                        round(ST_Area(ST_Transform(ST_Intersection(A.shape, B.shape), 3116))::numeric, 2) AS Area_Intersect_Ha
                                                    FROM public.departamentos A, public.resguardo B
                                                    WHERE A.codigo_departamento = %s
                                                    AND ST_Intersects(A.shape, B.shape)
                                                    ORDER BY B.id_resguardo, A.codigo_departamento''', [coddane])
    serializer = resultadosIntersect(resultadosIntersect, many=True)
    return Response(serializer.data)
