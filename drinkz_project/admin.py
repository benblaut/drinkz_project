from recipes.models import Recipes, Ingredient
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
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

user_admin_site = UserAdmin(name='usersadmin')

user_admin_site.register(Recipes, RecipesAdmin)
user_admin_site.register(Ingredient)
