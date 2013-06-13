from recipes.models import Recipes, Ingredient
from bottles.models import Bottle
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django import forms
from drinkz_project.forms import UserAdminAuthenticationForm
 
class UserAdmin(AdminSite):
    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active

class RecipesAdmin(admin.ModelAdmin):
    model = Recipes
    filter_horizontal = ('ingredients',)

class BottleForm(forms.ModelForm): 
    typ = forms.ChoiceField(widget = forms.Select(), choices = [])
   
    def __init__(self, *args, **kwargs):
        super(BottleForm, self).__init__(*args, **kwargs)
        items = Ingredient.objects.values_list('part', flat=True).distinct()
        self.fields['typ'].choices = [(item, item) for item in items]

class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    form = BottleForm

user_admin_site = UserAdmin(name='usersadmin')

user_admin_site.register(Recipes, RecipesAdmin)
user_admin_site.register(Ingredient)
user_admin_site.register(Bottle, BottleAdmin)
