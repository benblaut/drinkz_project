from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from drinkz_project import settings
from drinkz_project.admin import user_admin_site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'drinkz_project.views.home', name='home'),

    url(r'^users/', include('registration.backends.default.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^dashboard/', include(user_admin_site.urls)),

    url(r'^recipes/', include('recipes.urls')),

    url(r'^bottles/', include('bottles.urls')),

    url(r'^parties/', include('parties.urls')),
)
