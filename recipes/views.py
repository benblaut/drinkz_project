from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from recipes.models import Recipes, Ingredient
from recipes.forms import RecipesForm, IngredientForm
from django.template import RequestContext, Context, loader 

def recipes(request):
    recipes_list = Recipes.objects.all()
    t = loader.get_template('recipes/recipes.html')
    c = Context({'recipes_list': recipes_list,})
    return HttpResponse(t.render(c))

def add_recipe(request):
    recipes_list = Recipes.objects.all()
    form = RecipesForm(request.POST or None)
    if form.is_valid():
        rmodel = form.save()
        rmodel.save()
        return redirect(recipes)

    return render_to_response('recipes/add_recipe.html',
                              {'recipes_list': recipes_list, 'recipe_add': form},
                              context_instance=RequestContext(request))

def add_ingredient(request):
    ingredient_list = Ingredient.objects.all()
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        imodel = form.save()
        imodel.save()
        return redirect(add_recipe)

    return render_to_response('recipes/add_ingredient.html',
                              {'ingredient_add': form,},
                              context_instance=RequestContext(request))
    
