from django.db import models
from recipes.models import Ingredient
from django.template.defaultfilters import slugify

class Bottle(models.Model):
    mfg = models.CharField(max_length=100)
    liquor = models.CharField(max_length=100)
    typ = models.OneToOneField(Ingredient)

    def __unicode__(self):
        return self.mfg + ", " + self.liquor + ", " + self.typ

    def class_name(self):
        return "%s" % (slugify(self.name))

   # def unique_types(self):
        #return Bottle.objects.values_list('typ', flat=True).distinct()
