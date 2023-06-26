from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('recettes-sucrees/', views.recettes_sucrees, name='recettes_sucrees'),
    path('recettes-salees/', views.recettes_salees, name='recettes_salees'),
    path('recette/<int:recette_id>/', views.recette_detail, name='recette_detail'),
]