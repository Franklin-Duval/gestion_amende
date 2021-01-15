from django.urls import path, include
from rest_framework import routers

from . import views

routers = routers.DefaultRouter()
routers.register(r'admin', views.AdminViewSet)
routers.register(r'amende', views.AmendeViewSet)
routers.register(r'bd_police', views.BD_PoliceViewSet)
routers.register(r'infraction', views.InfractionViewSet)
routers.register(r'fuyard', views.FuyardViewSet)
routers.register(r'vehicule', views.Matricule_VehiculeViewSet)
routers.register(r'policier', views.Controlleur_RoutierViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    path('auth-login/', views.login),
    path('getuser/', views.getUser)
]