from django.contrib import admin

from .models import Recette,Categorie


# Register your models here.
admin.site.register(Recette)
admin.site.register(Categorie)