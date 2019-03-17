
from django.shortcuts import render, HttpResponse
import json
#from dash.tests import *

# Create your views here.
def send_back(request):
    
    post_text = request.POST.get('the_post')
    Msg_no = request.POST.get('appel_no')

    response_data = {}
    response_data['Msg_no'] = Msg_no
    response_data['zpost_contenu'] = post_text
    jason_obj=json.dumps(response_data)

    return HttpResponse(jason_obj,
            content_type="application/json")

def index(request,):
    """Return ."""
    context={'toto':'titi',}
    return render(request, 'dash/index.html',context)

