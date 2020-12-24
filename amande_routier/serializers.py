from .models import *
from rest_framework import serializers

class AdminSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Admin
        fields = [
            'id',
            'username',
            'password',
        ]

class BD_PoliceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BD_Police
        fields = [
            'id',
            'CNI',
            'nom',
            'prenom',
            'adresse',
            'contact',
            'date_naissance',
            'age',
            'statut_matrimoniale'
        ]

class Matricule_VehiculeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matricule_Vehicule
        fields = [
            'id',
            'matricule',
            'carte_grise',
            'proprietaire',
        ]

class Controlleur_RoutierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Controlleur_Routier
        fields = [
            'id',
            'CNI',
            'nom',
            'prenom',
            'adresse',
            'contact',
            'date_naissance',
            'age',
            'statut_matrimoniale',
            'num_identification',
            'nombre_amende',
            'user_name',
            'email',
            'password',
        ]

class FuyardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fuyard
        fields = [
            'id',
            'fuyeur',
            'nombre_infraction',
        ]

class AmendeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amende
        fields = [
            'id',
            'nom_amende',
            'desciption',
            'nombre_victimes',
            'prix_penalite',
        ]

class InfractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Infraction
        fields = [
            'id',
            'fuyard',
            'amende',
            'policier',
            'date',
            'payé',
        ]