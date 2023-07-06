from django.shortcuts import render

# Create your views here.


def dashboard(request):
    
    return render(request, 'dash/dashboard.html')

def cmr(request):
    
    return render(request, 'dash/cmr.html')
