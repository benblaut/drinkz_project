from django.shortcuts import render_to_response, redirect, get_object_or_404
from recipes.models import Recipes, Ingredient
#from recipes.forms import RecipesForm, IngredientForm
from django.template import RequestContext

def recipes(request):
    recipes_list = Recipes.objects.all()
    return render_to_response('recipes/recipes.html', {'recipes_list': recipes_list,}, 
                              context_instance=RequestContext(request))
    
