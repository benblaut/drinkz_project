from django.conf.urls import patterns, include, url
from django.contrib import admin
from drinkz_project import settings
 
admin.autodiscover()
 
urlpatterns = patterns('',
    url(r'^$', 'parties.views.parties'),

    #url(r'^sort_by_mfg', 'bottles.views.bottles_by_mfg'),
)
