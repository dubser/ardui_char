from django.shortcuts import render

# Create your views here.

def testSD(request,):
    """Return the last five published questions."""
    context={'toto':'titi',}
    return render(request, 'dash/testsd.html',context)
def bootstrap(request,):
    """Return the last five published questions."""
    context={'toto':'titi',}
    return render(request, 'dash/bootstrap.html',context)
