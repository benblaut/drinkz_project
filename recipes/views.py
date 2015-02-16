from django.shortcuts import render_to_response, redirect, get_object_or_404
from recipes.models import Recipes, Ingredient
from bottles.models import Bottle
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import unicodedata

@login_required
def recipes(request):
    recipes_list = Recipes.objects.all()
    inventory = Bottle.objects.filter(user=request.user)

    types_needed = []
    ingredients_needed = []
    mixable_recs = []
    partial_recs = []

    for rec in recipes_list:
        needs_ingredients = False
        has_some_ingredients = False
        ings = rec.ingredients.all()
        for i in ings:
            brands_owned = []
            amt = convert_to_ml(i.amount)
            typ = i.part
            brands_owned = check_inventory_for_type(inventory, typ, brands_owned)
            if len(brands_owned) == 0:
                needs_ingredients = True
                types_needed.append((unicodedata.normalize('NFKD', rec.name).encode('ascii', 'ignore'), typ, amt))
            else:
                amounts_from_brands = []

                for (m, l) in brands_owned:
                    amount_owned_of_brand = get_liquor_amount(inventory, m, l)
                    amounts_from_brands.append(amount_owned_of_brand)
                if (amount_owned_of_brand <= amt):
                    needs_ingredients = True
                    has_some_ingredients = True
                    amount_needed = amt - amount_owned_of_brand
                    ingredients_needed.append((unicodedata.normalize('NFKD', rec.name).encode('ascii', 'ignore'), unicodedata.normalize('NFKD', typ).encode('ascii', 'ignore'), amount_needed))

        if not needs_ingredients:
            mixable_recs.append(rec)

        if has_some_ingredients:
           partial_recs.append(rec)

    for (rec_name, type_needed, amount_needed) in types_needed:
        ingredients_needed.append((rec_name, unicodedata.normalize('NFKD', type_needed).encode('ascii', 'ignore'), amount_needed))   

    print (partial_recs)
    return render_to_response('recipes/recipes.html', {'recipes_list': recipes_list, 'ingredients_needed': ingredients_needed, 'mixable_recs': mixable_recs, 'partial_recs': partial_recs,}, 
                              context_instance=RequestContext(request))    

@login_required
def recipes_by_rating(request):
    recipes_list_by_rating = Recipes.objects.all()
    recipes_list_by_rating = recipes_list_by_rating.extra(select={
      'rating_int': '((100/%s*rating_score/(rating_votes+%s))+100)/2' % (Recipes.rating.range, Recipes.rating.weight)
    })
    recipes_list_by_rating = recipes_list_by_rating.order_by('-rating_int')
    inventory = Bottle.objects.filter(user=request.user)

    types_needed = []
    ingredients_needed = []
    mixable_recs = []
    partial_recs = []

    for rec in recipes_list_by_rating:
        needs_ingredients = False
        has_some_ingredients = False
        ings = rec.ingredients.all()
        for i in ings:
            brands_owned = []
            amt = convert_to_ml(i.amount)
            typ = i.part
            brands_owned = check_inventory_for_type(inventory, typ, brands_owned)
            if len(brands_owned) == 0:
                needs_ingredients = True
                types_needed.append((unicodedata.normalize('NFKD', rec.name).encode('ascii', 'ignore'), typ, amt))
            else:
                amounts_from_brands = []

                for (m, l) in brands_owned:
                    amount_owned_of_brand = get_liquor_amount(inventory, m, l)
                    amounts_from_brands.append(amount_owned_of_brand)
                if (amount_owned_of_brand <= amt):
                    needs_ingredients = True
                    has_some_ingredients = True
                    amount_needed = amt - amount_owned_of_brand
                    ingredients_needed.append((unicodedata.normalize('NFKD', rec.name).encode('ascii', 'ignore'), unicodedata.normalize('NFKD', typ).encode('ascii', 'ignore'), amount_needed))

        if not needs_ingredients:
           mixable_recs.append(rec)

        if has_some_ingredients:
           partial_recs.append(rec)

    for (rec_name, type_needed, amount_needed) in types_needed:
        ingredients_needed.append((rec_name, unicodedata.normalize('NFKD', type_needed).encode('ascii', 'ignore'), amount_needed))    

    return render_to_response('recipes/recipes_by_rating.html', {'recipes_list_by_rating': recipes_list_by_rating, 'ingredients_needed': ingredients_needed, 'mixable_recs': mixable_recs, 'partial_recs': partial_recs,}, 
                              context_instance=RequestContext(request))

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
        print ("\nIncorrect unit of measurement, use ml, g, or oz.")

def check_inventory_for_type(inventory, typ, brands_owned):
    for b in inventory:
        if b.typ == typ:
            brands_owned.append((b.mfg, b.liquor))

    return brands_owned

def get_liquor_amount(inventory, mfg, liquor):
    "Retrieve the total amount of any given liquor currently in inventory."
    amounts = [] 
    found = False
    for b in inventory:
        if b.mfg == mfg and b.liquor == liquor:
            found = True
            ml_amount = convert_to_ml(b.amount)           
            amounts.append(ml_amount)
            total = sum(amounts)
            
            return total

    if not found:
        err = "Missing liquor: manufacturer '%s', name '%s'" % (mfg, liquor)
        raise LiquorMissing(err)
