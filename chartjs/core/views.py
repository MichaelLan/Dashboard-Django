from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core import serializers
from .models import Proyecto

from django.http import HttpResponse

# Create your views here.
class graphPageView(TemplateView):
    template_name = 'index.html'

def getDataId(request, id):
    # labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    # datasets = {'name': 'My First dataset',
    #         'labels': ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    #         'data': [40, 10, 5, 2, 20, 30, 45]}
    datasets = serializers.serialize('json', Proyecto.objects.filter(id=id))
    
    return HttpResponse(datasets)
