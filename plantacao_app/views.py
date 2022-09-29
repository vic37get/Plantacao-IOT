import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from utils import temperaturaMinima, temperaturaMaxima, umidadeMinima, umidadeMaxima
from utils import connectMongo
from bson.objectid import ObjectId

db_client = connectMongo('PlantacaoIOT')

# Create your views here.
def home(request):
    collection_aplicacaoData = db_client['AplicacaoData']
    dados = collection_aplicacaoData.find_one({})
    template = loader.get_template('plantacao_app/home.html')
    context={
        'temperatura_dht11': dados['temperatura'],
        'chuva': dados['chuva'],
        'onOff': dados['onOff'],
        'umidade_dht11': dados['umidadeAr'],
        'umidade_solo': dados['umidadeSolo'],
        'temperatura_minima': temperaturaMinima(),
        'temperatura_maxima': temperaturaMaxima(),
        'umidade_minima': umidadeMinima(),
        'umidade_maxima': umidadeMaxima(),
    }
    return HttpResponse(template.render(context, request))

def led(request):
    return JsonResponse({'led': 'on'})

@csrf_exempt
def recebe_informacoes(request):
    collection_AplicacaoData = db_client['AplicacaoData']
    dados = request.GET
    registro_banco = collection_AplicacaoData.find_one({})
    collection_AplicacaoData.update_one({'_id': ObjectId(registro_banco['_id'])},{'$set':dados},upsert=True)
    response_data = dados
    return HttpResponse(json.dumps(response_data), content_type="application/json")