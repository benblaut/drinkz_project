from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from drinkz_project import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'drinkz_project.views.home', name='home'),

    url(r'^users/', include('registration.backends.default.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^recipes/', include('recipes.urls')),
)
