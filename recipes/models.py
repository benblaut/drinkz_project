from django.db import models

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name + " / " + self.ingredients

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
