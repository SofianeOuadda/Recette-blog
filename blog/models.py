from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Recette(models.Model):
    titre = models.CharField(max_length=200)
    temps_cuisson = models.CharField(max_length=100)
    temps_preparation = models.CharField(max_length=100)
    ingredients = models.TextField()
    etapes_preparation = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    difficulte = models.IntegerField(choices=((1, 'Facile'), (2, 'Moyenne'), (3, 'Difficile')))
    nombre_personnes = models.PositiveIntegerField()
    date_creation = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.titre

class Ingredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return self.ingredient
