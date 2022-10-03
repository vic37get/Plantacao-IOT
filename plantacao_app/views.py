import json

from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from utils import (temperaturaMaxima, temperaturaMinima, umidadeMaxima,
                   umidadeMinima)


def home(request):
    with open('informacoes.json', 'r') as f:
        dados = json.load(f)
    template = loader.get_template('plantacao_app/home.html')
    
    context={
        'temperatura_dht11': dados['temperatura'],
        'chuva': dados['chuva'],
        'status': dados['status'],
        'umidade_dht11': dados['umidadeAr'],
        'umidade_solo': dados['umidadeSolo'],
        'temperatura_minima': temperaturaMinima(),
        'temperatura_maxima': temperaturaMaxima(),
        'umidade_minima': umidadeMinima(),
        'umidade_maxima': umidadeMaxima(),
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def recebe_informacoes(request):
    response_data = request.GET
    json_dados = json.dumps(response_data, indent=4)
    with open('informacoes.json', 'w') as f:
        f.write(json_dados)
    print(response_data)
    return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def result_response(request):
    with open('informacoes.json', 'r') as f:
        dados = json.load(f)
    return HttpResponse(json.dumps(dados), content_type="application/json")



