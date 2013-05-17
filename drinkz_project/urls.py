from django.conf.urls import patterns, include, url
from djangoratings.views import AddRatingFromModel

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from drinkz_project import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drinkz_project.views.home', name='home'),
    # url(r'^drinkz_project/', include('drinkz_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^recipes/$', 'recipes.views.recipes'),

    url(r'^recipes/add_recipe/$', 'recipes.views.add_recipe'),

    url(r'rate/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(), {
        'app_label': 'recipes',
        'model': 'recipes',
        'field_name': 'rating',
    }),
)
