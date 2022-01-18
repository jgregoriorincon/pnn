from django.urls import path
from apps.intersect.api.api import IntersectAPIViewArea, IntersectAPIViewDpto

urlpatterns = [
    path('area/', IntersectAPIViewArea.as_view(), name='Intersect_Area'),
    path('dpto/', IntersectAPIViewDpto.as_view(), name='Intersect_Dpto')
]