from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from home.models import samplemodel

def index(request):
    context = {"a": ""}
    return render(request, 'index.html', context)

def run(request):
    print(request)
    if request.method == 'POST':
        data = {}
        data['firstName'] = request.POST.get('firstName')
        data['lastName'] = request.POST.get('lastName')
        data['phone'] = request.POST.get('phoneNumber')
        print(data)
    context = {"a": "Data submitted"}
    return render(request, 'index.html', context)

# Create your views here.
