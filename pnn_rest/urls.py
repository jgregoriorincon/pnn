from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('intersect/', include('apps.intersect.api.urls')),
    path('print/', include('apps.print.urls')),
    path('admin/', admin.site.urls),
]
