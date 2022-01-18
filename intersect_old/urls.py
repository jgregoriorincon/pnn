from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.ShowAll, name='all'),
    path('dpto/<str:coddane>/', views.ShowAll, name='dpto'),
]