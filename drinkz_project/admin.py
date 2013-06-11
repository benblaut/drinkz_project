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

'''class RecipesForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(RecipesForm, self).__init__(*args, **kwargs)
        wtf = Ingredient.objects.values_list('part', flat=True).distinct()
        w = self.fields['ingredients'].widget
        choices = []
        for choice in wtf:
            choices.append(choice.name)
        w.choices = choices'''

class RecipesAdmin(admin.ModelAdmin):
    model = Recipes
    filter_horizontal = ('ingredients',)
    #form = RecipesForm

user_admin_site = UserAdmin(name='usersadmin')

user_admin_site.register(Recipes, RecipesAdmin)
user_admin_site.register(Ingredient)
user_admin_site.register(Bottle)
