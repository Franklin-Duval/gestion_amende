from django.shortcuts import redirect

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.

class AdminViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows classes to be viewed or modified
    """
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class BD_PoliceViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows subjects to be viewed or modified
    """
    queryset = BD_Police.objects.all()
    serializer_class = BD_PoliceSerializer

class Matricule_VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Matricule_Vehicule.objects.all()
    serializer_class = Matricule_VehiculeSerializer

class Controlleur_RoutierViewSet(viewsets.ModelViewSet):
    queryset = Controlleur_Routier.objects.all()
    serializer_class = Controlleur_RoutierSerializer

class InfractionViewSet(viewsets.ModelViewSet):
    queryset = Infraction.objects.all()
    serializer_class = InfractionSerializer

class FuyardViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows comments to be viewed or modified
    """
    queryset = Fuyard.objects.all()
    serializer_class = FuyardSerializer

class AmendeViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to subscribe to a course
    """
    queryset = Amende.objects.all()
    serializer_class = AmendeSerializer


@api_view(['GET'])
def errorPage(request):
    
    result = {
        "code": "HTTP_404_NOT_FOUND",
        "status": "Page not found",
        "message": "Vérifiez votre URL"
    }

    return Response(result, status=status.HTTP_404_NOT_FOUND)


def root(request):
    return redirect('/api')