from django.shortcuts import render_to_response, redirect
from bottles.models import Bottle
from bottles.admin import BottleForm
from recipes.models import Ingredient
from recipes.views import convert_to_ml
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def bottles(request):
    bottle_list = Bottle.objects.filter(user=request.user)
    type_list = []
    type_amounts = {}

    for bottle in bottle_list:
        if bottle.typ not in type_list:
            type_list.append(bottle.typ)

    for t in type_list:
        type_amount = get_liquor_amount_by_type(bottle_list, t)
        type_amounts[t] = type_amount

    return render_to_response('bottles/bottles.html', {'bottles_list': bottle_list, 'type_list': type_list, 'type_amounts': type_amounts,}, 
                              context_instance=RequestContext(request))

@login_required 
def bottles_by_mfg(request):
    bottle_list = Bottle.objects.filter(user=request.user)
    mfg_list = []
    for bottle in bottle_list:
        if bottle.mfg not in mfg_list:
            mfg_list.append(bottle.mfg)

    return render_to_response('bottles/bottles_by_mfg.html', {'bottles_list': bottle_list, 'mfg_list': mfg_list,}, 
                              context_instance=RequestContext(request))

def get_liquor_amount_by_type(bottle_list, typ):
    amounts = []
    for bottle in bottle_list:
        if bottle.typ == typ:
            ml_amount = convert_to_ml(bottle.amount)
            amounts.append(ml_amount)
            total = sum(amounts)
            print len(bottle_list)

            return str(total) + " ml"
