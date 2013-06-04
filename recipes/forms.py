from django.forms import ModelForm, TextInput
import recipes.models
from recipes.models import Recipes, Ingredient

class RecipesForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ['name', 'ingredients',]
        widgets = {
            'name': TextInput(attrs={'id': 1,}),
        }

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['part', 'amount',]
