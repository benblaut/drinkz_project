from django.shortcuts import render_to_response, redirect, get_object_or_404
from bottles.models import Bottle
from django.template import RequestContext

def bottles(request):
    bottle_list = Bottle.objects.all()
    return render_to_response('bottles/bottles.html', {'bottles_list': bottle_list,}, 
                              context_instance=RequestContext(request))
    
