from django.shortcuts import render, get_object_or_404, redirect
from .models import Recette, Ingredient
from .forms import IngredientForm


def accueil(request):
    return render(request, 'blog/accueil.html')

def recettes_sucrees(request):
    recettes_sucrees = Recette.objects.filter(categorie__nom='Sucré')
    context = {
        'recettes_sucrees': recettes_sucrees
    }
    return render(request, 'blog/recettes_sucrees.html', context)

def recettes_salees(request):
    recettes_salees = Recette.objects.filter(categorie__nom='Salé')
    context = {
        'recettes_salees': recettes_salees
    }
    return render(request, 'blog/recettes_salees.html', context)



def recette_detail(request, recette_id):
    recette = get_object_or_404(Recette, id=recette_id)
    ingredients_list = recette.ingredients.split('\n')

    forms = []
    for ingredient in ingredients_list:
        form_data = {'ingredient': ingredient}
        form = IngredientForm(form_data)
        forms.append(form)

    if request.method == 'POST':
        for form in forms:
            form_data = {
                'ingredient': form['ingredient'].value(),
                'checked': form['checked'].value()
            }
            form = IngredientForm(form_data)
            if form.is_valid():
                form.save()

        return redirect('recette_detail', recette_id=recette_id)

    context = {
        'recette': recette,
        'forms': forms
    }
    return render(request, 'blog/recette_detail.html', context)
