from django.shortcuts import render
from .models import design
def home_view(request):
    obj = design.objects.values()
    context = {
        'design':obj
    }
    return render(request,'home.html',context)
# Create your views here.
