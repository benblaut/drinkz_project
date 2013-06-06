from django.conf.urls import patterns, include, url
from djangoratings.views import AddRatingFromModel
from django.contrib import admin
from drinkz_project import settings
from drinkz_project.admin import user_admin_site
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^$', 'recipes.views.recipes'),

    url(r'^dashboard/', include(user_admin_site.urls)),

    url(r'rate/(?P<object_id>\d+)/(?P<score>\d+)/', AddRatingFromModel(), {
        'app_label': 'recipes',
        'model': 'recipes',
        'field_name': 'rating',
    }),
)
