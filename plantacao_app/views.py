import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from utils import temperaturaMinima, temperaturaMaxima, umidadeMinima, umidadeMaxima


# Create your views here.
def home(request):
    template = loader.get_template('plantacao_app/home.html')
    context={
        'temperatura_minima': temperaturaMinima(),
        'temperatura_maxima': temperaturaMaxima(),
        'umidade_minima': umidadeMinima(),
        'umidade_maxima': umidadeMaxima()
    }
    return HttpResponse(template.render(context, request))

def led(request):
    return JsonResponse({'led': 'on'})
