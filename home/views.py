from django.shortcuts import render
from django.http import HttpResponse
from home.models import samplemodel

def index(request):
    print(samplemodel.objects.get(number=123))
    return render(request, 'index.html', {"data": "laxman"})

# Create your views here.
