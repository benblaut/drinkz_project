from recipes.models import Recipes, Ingredient
from bottles.models import Bottle
from parties.models import Party
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django import forms
from drinkz_project.forms import UserAdminAuthenticationForm, BottleForm, PartyForm
 
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

class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    form = BottleForm

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class PartyAdmin(admin.ModelAdmin):
    model = Party
    form = PartyForm

    def __init__(self, model, user_admin_site):
        self.form.user_admin_site = user_admin_site 
        super(PartyAdmin, self).__init__(model, user_admin_site)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PartyAdmin, self).get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form

    def save_model(self, request, obj, form, change):
        obj.host_user = request.user
        obj.save()

user_admin_site = UserAdmin(name='usersadmin')

user_admin_site.register(Recipes, RecipesAdmin)
user_admin_site.register(Ingredient)
user_admin_site.register(Bottle, BottleAdmin)
user_admin_site.register(Party, PartyAdmin)
