import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from utils import previsão_tempo


# Create your views here.
def home(request):
    template = loader.get_template('plantacao_app/home.html')
    context={

    }
    previsão_tempo()
    return HttpResponse(template.render(context, request))

def led(request):
    return JsonResponse({'led': 'on'})


