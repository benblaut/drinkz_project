from django.shortcuts import render_to_response, redirect
from bottles.models import Bottle
from parties.models import Party
from recipes.views import convert_to_ml
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

@login_required
def parties(request):
    party_list = Party.objects.filter(host_user=request.user)

    if not party_list:
      party_list = Party.objects.filter(guests=request.user)

    return render_to_response('parties/parties.html', {'party_list': party_list,},
                              context_instance=RequestContext(request))
