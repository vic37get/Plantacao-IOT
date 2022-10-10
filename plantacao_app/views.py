import json

from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from utils import (temperaturaMaxima, temperaturaMinima, umidadeMaxima,
                   umidadeMinima)
#from utils import connectMongo

#db_client = connectMongo('PlantacaoIOT')

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
        'temperatura_minima': dados['temperatura_minima'],
        'temperatura_maxima': dados['temperatura_maxima'],
        'umidade_minima': dados['umidade_minima'],
        'umidade_maxima': dados['umidade_maxima'],
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def recebe_informacoes(request):
    #collection_data = db_client['AplicacaoData']
    #collection_token = db_client['token']
    #auth = collection_token.find_one({})
    token = "35287412"
    dados = request.GET
    if len(dados) == 6 and dados['token'] == token:
        json_dados = json.dumps(dados, indent=4)
        json_dados = json.loads(json_dados)
        previsao_tempo = {
        'temperatura_minima': temperaturaMinima(),
        'temperatura_maxima': temperaturaMaxima(),
        'umidade_minima': umidadeMinima(),
        'umidade_maxima': umidadeMaxima(),
        }
        json_dados.update(previsao_tempo)
        del json_dados['token']
        with open('informacoes.json', 'w') as f:
            json.dump(json_dados, f)
        
        #collection_data.insert_one(json_dados)
        del json_dados['_id']
        return HttpResponse(json.dumps(json_dados), content_type="application/json")
    else:
        return HttpResponseForbidden()

@csrf_exempt
def result_response(request):
    with open('informacoes.json', 'r') as f:
        dados = json.load(f)
    return HttpResponse(json.dumps(dados), content_type="application/json")
