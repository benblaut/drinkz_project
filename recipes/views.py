from django.http import HttpResponse
from recipes.models import Recipes
from django.template import Context, loader 

def index(request):
    recipes_list = Recipes.objects.all()
    t = loader.get_template('recipes/index.html')
    c = Context({'recipes_list': recipes_list,})
    return HttpResponse(t.render(c))
    
