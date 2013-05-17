from django.http import HttpResponse
from recipes.models import Recipes
from django.template import Context, loader 

def recipes(request):
    recipes_list = Recipes.objects.all()
    t = loader.get_template('recipes/recipes.html')
    c = Context({'recipes_list': recipes_list,})
    return HttpResponse(t.render(c))

def add_recipe(request):
    recipes_list = Recipes.objects.all()
    t = loader.get_template('admin/drinkz_project/recipes/add_recipe.html')
    c = Context({'recipes_list': recipes_list,})
    return HttpResponse(t.render(c))
    
