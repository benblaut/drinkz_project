from bottles.models import Bottle
from django.contrib import admin
from django import forms
from recipes.models import Ingredient

class BottleForm(forms.ModelForm): 
    typ = forms.ChoiceField(widget = forms.Select(), choices = [])
   
    def __init__(self, *args, **kwargs):
        super(BottleForm, self).__init__(*args, **kwargs)
        items = Ingredient.objects.values_list('part', flat=True).distinct()
        self.fields['typ'].choices = [(item, item) for item in items]

class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    form = BottleForm

admin.site.register(Bottle, BottleAdmin)
