from recipes.models import Recipes, Ingredient
from django.contrib import admin

class RecipesAdmin(admin.ModelAdmin):
    model = Recipes
    filter_horizontal = ('ingredients',)

admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Ingredient)
