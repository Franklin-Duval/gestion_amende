from django.shortcuts import redirect

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class BD_PoliceViewSet(viewsets.ModelViewSet):
    queryset = BD_Police.objects.all().order_by('id')
    serializer_class = BD_PoliceSerializer

class Matricule_VehiculeViewSet(viewsets.ModelViewSet):
    queryset = Matricule_Vehicule.objects.all().order_by('id')
    serializer_class = Matricule_VehiculeSerializer

class Controlleur_RoutierViewSet(viewsets.ModelViewSet):
    queryset = Controlleur_Routier.objects.all().order_by('id')
    serializer_class = Controlleur_RoutierSerializer

class InfractionViewSet(viewsets.ModelViewSet):
    queryset = Infraction.objects.all().order_by('id')
    serializer_class = InfractionSerializer

    def create(self, request, *args, **kwargs):
        meta = {}

        idVictime = request.data["fuyard"]
        idAmende = request.data["amende"]
        idPolicier = request.data["policier"]

        #recupérer les id à partir des liens
        idVictime = idVictime[idVictime.find("fuyard")+7: ]
        idVictime = int(idVictime.replace("/", ""))

        idAmende = idAmende[idAmende.find("amende")+7: ]
        idAmende = int(idAmende.replace("/", ""))

        idPolicier = idPolicier[idPolicier.find("policier")+9: ]
        idPolicier = int(idPolicier.replace("/", ""))

        #recupérer les instances avec les id
        victime = Fuyard.objects.get(pk=idVictime)
        amende = Amende.objects.get(pk=idAmende)
        policier = Controlleur_Routier.objects.get(pk=idPolicier)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        meta["status"] = "SUCCESS"
        meta["result"] = serializer.data

        #increment values
        victime.increment_infraction()
        amende.increment_victime()
        policier.increment_amende()

        headers = self.get_success_headers(serializer.data)
        return Response(meta, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        meta = {"status": "impossible de détruire"}
        return Response(meta, status=status.HTTP_401_UNAUTHORIZED)


class FuyardViewSet(viewsets.ModelViewSet):
    queryset = Fuyard.objects.all().order_by('id')
    serializer_class = FuyardSerializer

class AmendeViewSet(viewsets.ModelViewSet):
    queryset = Amende.objects.all().order_by('id')
    serializer_class = AmendeSerializer


@api_view(['GET', 'POST'])
def login(request):

    if (("username" not in request.data) or ("password" not in request.data) or ("type" not in request.data)):
        result = {
            "status": "FAILURE",
            "code": "HTTP_400_BAD_REQUEST",
            "message": "Only username, password and type fields are accepted",
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
        
    if (request.method=='POST'):
        username = request.data["username"]
        password = request.data["password"]
        type = request.data["type"]
        
        try:
            if (type == "admin"):
                Admin.objects.get(username=username, password=password)
            elif (type == "policier"):
                Controlleur_Routier.objects.get(user_name=username, password=password)
            else:
                return Response({"status": "error type"}, status=status.HTTP_200_OK)
            
            result = {
                "code": "HTTP_200_OK",
                "login": "SUCCESS",
                "user": username,
                "type": type
            }
            return Response(result, status=status.HTTP_200_OK)
        except:
            result = {
                "code": "HTTP_401_UNAUTHORIZED",
                "login": "FAILED",
                "message": "verifiez votre username et password"
            }
            return Response(result)     

@api_view(['GET', 'POST'])
def getUser(request):
    usager = {}
    if (request.method=='POST'):
        try:
            if ("CNI" in request.data):
                user = BD_Police.objects.get(CNI = request.data["CNI"])
                print(user.id)
                try:
                    voiture = Matricule_Vehicule.objects.get(proprietaire = user.id)
                    usager = {
                        "id_usager": user.id,
                        "CNI": user.CNI,
                        "nom": user.nom,
                        "prenom": user.prenom,
                        "adresse": user.adresse,
                        "contact": user.contact,
                        "date_naissance": user.date_naissance,
                        "age": user.age,
                        "statut_matrimoniale": user.statut_matrimoniale,
                        "id_voiture": voiture.id,
                        "matricule": voiture.matricule,
                        "carte_grise": voiture.carte_grise
                    }
                except:
                    usager = {
                        "id_usager": user.id,
                        "CNI": user.CNI,
                        "nom": user.nom,
                        "prenom": user.prenom,
                        "adresse": user.adresse,
                        "contact": user.contact,
                        "date_naissance": user.date_naissance,
                        "age": user.age,
                        "statut_matrimoniale": user.statut_matrimoniale
                    }
                
            elif ("matricule" in request.data):
                voiture = Matricule_Vehicule.objects.get(matricule = request.data["matricule"])
                
                prop = voiture.proprietaire.id
                user = BD_Police.objects.get(id = prop)
                usager = {
                    "id_usager": user.id,
                    "CNI": user.CNI,
                    "nom": user.nom,
                    "prenom": user.prenom,
                    "adresse": user.adresse,
                    "contact": user.contact,
                    "date_naissance": user.date_naissance,
                    "age": user.age,
                    "statut_matrimoniale": user.statut_matrimoniale,
                    "id_voiture": voiture.id,
                    "matricule": voiture.matricule,
                    "carte_grise": voiture.carte_grise
                }
            else:
                return Response({"status": "Only Matricule and CNI are accepted"}, status=status.HTTP_200_OK)
        except:
            result = {
                "code": "HTTP_401_UNAUTHORIZED",
                "status": "FAILED",
                "message": "User not found"
            }
            return Response(result)

        return Response(usager, status=status.HTTP_200_OK)

    

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