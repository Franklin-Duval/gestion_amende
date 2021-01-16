from django.db import models
from django.db.models.base import Model

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=20, null=False, unique=True)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.username


class BD_Police(models.Model):
    STATUT = (
        (1, 'Célibataire'),
        (2, 'Marié'),
        (3, 'Compliqué')
    )

    CNI = models.IntegerField(unique=True, null=False)
    nom = models.CharField(max_length=50, null=False)
    prenom = models.CharField(max_length=50, null=False)
    adresse = models.CharField(max_length=50, null=False)
    contact = models.IntegerField(unique=True, null=False)
    date_naissance = models.DateField(null=True)
    age = models.PositiveIntegerField(default=0)
    statut_matrimoniale = models.IntegerField(choices=STATUT)

    def __str__(self):
        return str(self.CNI) + " " + self.nom


class Matricule_Vehicule(models.Model):
    matricule = models.CharField(max_length=15, null=False, unique=True)
    carte_grise = models.CharField(max_length=100, null=False, unique=True)
    proprietaire = models.ForeignKey(BD_Police, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricule + " " + self.carte_grise


class Controlleur_Routier(BD_Police):
    num_identification = models.IntegerField(unique=True, null=False)
    nombre_amende = models.IntegerField(default=0)
    user_name = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return str(self.num_identification) + " " + self.nom

    def increment_amende(self):
        self.nombre_amende = self.nombre_amende + 1
        self.save()

class Fuyard(models.Model):
    fuyeur = models.ForeignKey(BD_Police, on_delete=models.CASCADE, null=True)
    nombre_infraction = models.IntegerField(default=0, null=False)
    matricule_vehicule = models.CharField(max_length=15, unique=True, null=True)

    def __str__(self):
        return str(self.fuyeur.CNI) + " " + self.fuyeur.nom

    def increment_infraction(self):
        self.nombre_infraction = self.nombre_infraction + 1
        self.save()

class Amende(models.Model):
    nom_amende = models.CharField(max_length=50, null=False)
    desciption = models.TextField(null=True)
    nombre_victimes = models.IntegerField(default=0, null=False)
    prix_penalite = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.nom_amende

    def increment_victime(self):
        self.nombre_victimes = self.nombre_victimes + 1
        self.save()

class Infraction(models.Model):
    fuyard = models.ForeignKey(Fuyard, on_delete=models.CASCADE, null=False)
    amende = models.ForeignKey(Amende, on_delete=models.CASCADE, null=False)
    policier = models.ForeignKey(Controlleur_Routier, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    lieux = models.CharField(max_length=50, null=True)
    payé = models.BooleanField(default=False)

    def __str__(self):
        return str(self.fuyard.CNI) + " " + self.date
