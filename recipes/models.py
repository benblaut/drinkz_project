from django.db import models
from django.template.defaultfilters import slugify
from djangoratings.fields import RatingField

class Ingredient(models.Model):
    UNIT = (
        ('1.5 oz', '1 shot'),
        ('3 oz', '2 shots'),
        ('4.5 oz', '3 shots'),
        ('6 oz', '4 shots'),
        ('1 oz', '1 oz'),
        ('2 oz', '2 oz'),
        ('3 oz', '3 oz'),
        ('4 oz', '4 oz'),
        ('5 oz', '5 oz'),
        ('6 oz', '6 oz'),
        ('7 oz', '7 oz'),
        ('8 oz', '8 oz'),
        ('9 oz', '9 oz'),
        ('10 oz', '10 oz'),
        ('11 oz', '11 oz'),
        ('12 oz', '12 oz'),
    )
    part = models.CharField(max_length=100)
    amount = models.CharField(max_length=15, choices=UNIT)

    def __unicode__(self):
        return self.part + ", " + self.amount

    class Meta:
        ordering = ['part']

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    rating = RatingField(range=5, can_change_vote=True)

    @property
    def ingredient_list(self):
        return list(self.ingredients.all())

    def __unicode__(self):
        return self.name

    def class_name(self):
        return "%s" % (slugify(self.name))

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
