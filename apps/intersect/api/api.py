from pathlib import Path
import environ

from rest_framework.response import Response
from rest_framework.views import APIView
from apps.intersect.models import Intersect
from apps.intersect.api.serializers import IntersectSerializer

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file="docker/.env")
NAME_LAYER1 = env("NAME_LAYER1")
FIELD_COD_LAYER1 = env("FIELD_COD_LAYER1")
FIELD_NAME_LAYER1 = env("FIELD_NAME_LAYER1")

NAME_LAYER2 = env("NAME_LAYER2")
FIELD_COD_LAYER2 = env("FIELD_COD_LAYER2")
FIELD_NAME_LAYER2 = env("FIELD_NAME_LAYER2")

class IntersectAPIViewDpto(APIView):    
    def get(self, request, *args, **kwargs):
        try:            
            coddane = request.query_params["coddane"]
            if coddane != None:
                sql = f"SELECT 1 AS id, A.{FIELD_COD_LAYER1} as codigo_departamento, A.{FIELD_NAME_LAYER1} as nombre_departamento, B.{FIELD_COD_LAYER2} AS id_area, B.{FIELD_NAME_LAYER2} AS nombre_area, round(ST_Area(ST_Transform(ST_Intersection(A.shape, B.shape), 3116))::numeric, 2) AS area_ha FROM public.{NAME_LAYER1} A, public.{NAME_LAYER2} B WHERE B.{FIELD_COD_LAYER2} IS NOT NULL AND ST_Intersects(A.shape, B.shape) AND A.{FIELD_COD_LAYER1} = '{coddane}' ORDER BY B.{FIELD_COD_LAYER2}, A.{FIELD_COD_LAYER1}"

                resultadosIntersect = Intersect.objects.raw(sql)
                intersect_serizalizer = IntersectSerializer(resultadosIntersect, many=True)
        except:
            sql = f"SELECT 1 AS id, A.{FIELD_COD_LAYER1} as codigo_departamento, A.{FIELD_NAME_LAYER1} as nombre_departamento, B.{FIELD_COD_LAYER2} AS id_area, B.{FIELD_NAME_LAYER2} AS nombre_area, round(ST_Area(ST_Transform(ST_Intersection(A.shape, B.shape), 3116))::numeric, 2) AS area_ha FROM public.{NAME_LAYER1} A, public.{NAME_LAYER2} B WHERE B.{FIELD_COD_LAYER2} IS NOT NULL AND ST_Intersects(A.shape, B.shape) ORDER BY B.{FIELD_COD_LAYER2}, A.{FIELD_COD_LAYER1}"

            resultadosIntersect = Intersect.objects.raw(sql)
            intersect_serizalizer = IntersectSerializer(resultadosIntersect, many=True)
        return Response(intersect_serizalizer.data)

class IntersectAPIViewArea(APIView):    
    def get(self, request, *args, **kwargs):
        try:
            id_area = request.query_params["id"]
            if id_area != None:
                sql = f"SELECT 1 AS id, A.{FIELD_COD_LAYER1} as codigo_departamento, A.{FIELD_NAME_LAYER1} as nombre_departamento, B.{FIELD_COD_LAYER2} AS id_area, B.{FIELD_NAME_LAYER2} AS nombre_area, round(ST_Area(ST_Transform(ST_Intersection(A.shape, B.shape), 3116))::numeric, 2) AS area_ha FROM public.{NAME_LAYER1} A, public.{NAME_LAYER2} B WHERE B.{FIELD_COD_LAYER2} IS NOT NULL AND ST_Intersects(A.shape, B.shape) AND B.{FIELD_COD_LAYER2} = '{id_area}' ORDER BY B.{FIELD_COD_LAYER2}, A.{FIELD_COD_LAYER1}"

                resultadosIntersect = Intersect.objects.raw(sql)
                intersect_serizalizer = IntersectSerializer(resultadosIntersect, many=True)
        except:
            sql = f"SELECT 1 AS id, A.{FIELD_COD_LAYER1} as codigo_departamento, A.{FIELD_NAME_LAYER1} as nombre_departamento, B.{FIELD_COD_LAYER2} AS id_area, B.{FIELD_NAME_LAYER2} AS nombre_area, round(ST_Area(ST_Transform(ST_Intersection(A.shape, B.shape), 3116))::numeric, 2) AS area_ha FROM public.{NAME_LAYER1} A, public.{NAME_LAYER2} B WHERE B.{FIELD_COD_LAYER2} IS NOT NULL AND ST_Intersects(A.shape, B.shape) ORDER BY B.{FIELD_COD_LAYER2}, A.{FIELD_COD_LAYER1}"

            resultadosIntersect = Intersect.objects.raw(sql)
            intersect_serizalizer = IntersectSerializer(resultadosIntersect, many=True)
        return Response(intersect_serizalizer.data)
