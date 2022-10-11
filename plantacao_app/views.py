import json
from datetime import datetime, timezone

import pytz
from bdConect import connectMongo
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from utils import (temperaturaMaxima, temperaturaMinima, umidadeMaxima,
                   umidadeMinima)

db_client = connectMongo('PlantacaoIOT')

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
    collection_token = db_client['token']
    auth = collection_token.find_one()
    token = auth['token']
    dados = request.GET
    if len(dados) == 6 and dados['token'] == token:
        json_dados = json.dumps(dados, indent=4)
        json_dados = json.loads(json_dados)
        del json_dados['token']
        with open('informacoes.json', 'w', encoding=("Utf-8")) as f:
            json.dump(json_dados, f)
        return HttpResponse(json.dumps(json_dados), content_type="application/json")
    else:
        return HttpResponseForbidden()

@csrf_exempt
def result_response(request):
    with open('informacoes.json', 'r') as f:
        dados = json.load(f)
    return HttpResponse(json.dumps(dados), content_type="application/json")

@csrf_exempt
def saveInfo(request):
    collection_data = db_client['AplicacaoData']
    with open('informacoes.json', 'r') as f:
        dados = json.load(f)
    timezone = pytz.timezone('Brazil/East')
    time = datetime.now(timezone)
    dados['data'] = time.strftime("%m/%d/%Y %H:%M:%S")
    collection_data.insert_one(dados)
    return HttpResponse(request)

def deleteAllInfo(request):
    collection_data = db_client['AplicacaoData']
    collection_data.remove()
    messages.success(request, 'Os registros foram excluídos!')
    return redirect('/')
