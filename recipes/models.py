from django.db import models

class Ingredient(models.Model):
    part = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)

    def __unicode__(self):
        return self.part + ", " + self.amount

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)

    @property
    def ingredient_list(self):
        return list(self.ingredients.all())

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
