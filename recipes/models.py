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

    '''def need_ingredients(self):
        ings = list(self.ingredients.all())
        types_needed = []
        ingredients_needed = []
        for i in ings:
            amt = self.convert_to_ml(i.amount)
            ingredients_needed.append(amt)

        return ingredients_needed

    def convert_to_ml(amount):
        "Take a string of form (# unit), convert the # to ml and change unit to ml"
        amount_split = amount.split()
        float_amount = float(amount_split[0])
            
        if amount_split[1] == "ml" or amount_split[1] == "milliliter" or amount_split[1] == "milliliters":
            return float_amount
        elif amount_split[1] == "l" or amount_split[1] == "liter" or amount_split[1] == "liters":
            float_amount *= 1000
            return float_amount
        elif amount_split[1] == "oz" or amount_split[1] == "ounce" or amount_split[1] == "ounces":
            float_amount *= 29.5735
            return float_amount
        elif amount_split[1] == "gallons" or amount_split[1] == "gallon" or amount_split[1] == "g":
            float_amount *= 3785.41
            return float_amount
        else:
            print "\nIncorrect unit of measurement, use ml, g, or oz."'''

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
