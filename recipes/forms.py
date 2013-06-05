from django.forms import ModelForm
import recipes.models
from recipes.models import Recipes, Ingredient

class RecipesForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'ingredients',]

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['part', 'amount']
