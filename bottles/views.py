from django.shortcuts import render_to_response, redirect, get_object_or_404
from bottles.models import Bottle
from bottles.admin import BottleForm
from recipes.models import Ingredient
from django.template import RequestContext
from django.forms.models import modelformset_factory

def bottles(request):
    bottle_list = Bottle.objects.all()
    type_list = []
    for bottle in bottle_list:
        if bottle.typ not in type_list:
            type_list.append(bottle.typ)

    return render_to_response('bottles/bottles.html', {'bottles_list': bottle_list, 'type_list': type_list}, 
                              context_instance=RequestContext(request))
    
def bottles_by_mfg(request):
    bottle_list = Bottle.objects.all()
    mfg_list = []
    for bottle in bottle_list:
        if bottle.mfg not in mfg_list:
            mfg_list.append(bottle.mfg)

    return render_to_response('bottles/bottles_by_mfg.html', {'bottles_list': bottle_list, 'mfg_list': mfg_list,}, 
                              context_instance=RequestContext(request))
