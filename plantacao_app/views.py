import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def home(request):
    template = loader.get_template('plantacao_app/home.html')
    context={

    }
    return HttpResponse(template.render(context, request))

def led(request):
    return JsonResponse({'led': 'on'})


