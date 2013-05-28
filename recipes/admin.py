from recipes.models import Recipes, Ingredient
from django.contrib import admin
from django.db.models import ManyToOneRel
from django import forms

'''class IngredientsForm(forms.ModelForm):
    ingredient = forms.ModelMultipleChoiceField(queryset=Ingredient.objects.order_by('part'))

    def __init__(self, *args, **kwargs):
        super(IngredientsForm, self).__init__(*args, **kwargs)
        rel = ManyToOneRel(self.instance.ingredients.model, 'id') 
        self.fields['ingredient'].widget = RelatedFieldWidgetWrapper(self.fields['ingredient'].widget, rel, self.admin_site) 

    class Meta:
        model = Recipes'''

class RecipesAdmin(admin.ModelAdmin):
    model = Recipes
    filter_horizontal = ('ingredients',)
    '''exclude = ('ingredients',)
    form = IngredientsForm

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(RecipesAdmin, self).__init__(model, admin_site)'''

admin.site.register(Recipes, RecipesAdmin)
#admin.site.register(Recipes)
admin.site.register(Ingredient)
