from django.urls import path
from apps.intersect.api.api import IntersectAPIViewArea, IntersectAPIViewDpto

urlpatterns = [
    path('area/<idarea>', IntersectAPIViewArea.as_view(), name='Intersect_Area'),
    path('dpto/<coddane>', IntersectAPIViewDpto.as_view(), name='Intersect_Dpto')
]