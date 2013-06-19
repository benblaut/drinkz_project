from django.conf.urls import patterns, include, url
from djangoratings.views import AddRatingFromModel
from django.contrib import admin
from drinkz_project import settings
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^$', 'recipes.views.recipes'),

    url(r'^sort_by_rating', 'recipes.views.recipes_by_rating'),

    url(r'rate/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(), {
        'app_label': 'recipes',
        'model': 'recipes',
        'field_name': 'rating',
    }),
)
