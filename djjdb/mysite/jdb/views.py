from django.shortcuts import render,HttpResponse
from jdb.models import Variete, pot

# Create your views here.
def listDb(request,):

#   print (a)
#   a=a.filter(id__gt=3)
#   a=a.filter(nom__icontains='tom')
    a = Variete.objects.filter(nom__startswith='T') | Variete.objects.filter(desc__startswith='H')


    b = pot.objects.all()

    context={'qset':a,'xset':b}
 #   print (context)

    return render(request, 'jdb/listdb.html',context)