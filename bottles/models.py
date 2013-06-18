from django.db import models
from recipes.models import Ingredient
from django.contrib.auth.models import User

class Bottle(models.Model):
    mfg = models.CharField(max_length=100)
    liquor = models.CharField(max_length=100)
    typ = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.mfg + ", " + self.liquor + ", " + self.typ + ", " + self.amount
