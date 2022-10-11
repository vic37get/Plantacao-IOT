import encodings
import json

from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from utils import (temperaturaMaxima, temperaturaMinima, umidadeMaxima,
                   umidadeMinima)
from utils import connectMongo

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
    collection_data = db_client['AplicacaoData']
    #collection_token = db_client['token']
    #auth = collection_token.find_one()
    #print(auth)
    token = "35287412"
    #token = auth['token']
    dados = request.GET
    print("dadostoken: ", dados['token'])
    if len(dados) == 6 and dados['token'] == token:
        json_dados = json.dumps(dados, indent=4)
        json_dados = json.loads(json_dados)
        if json_dados['chuva'] == '1':
            json_dados['chuva'] = 'Sem chuva'
        else:
            json_dados['chuva'] = 'Chovendo'
        
        if json_dados['status'] == '1':
            json_dados['status'] = 'Ligado'
        else:
            json_dados['status'] = 'Desligado'
        #previsao_tempo = {
        #}
        #json_dados.update(previsao_tempo)
        del json_dados['token']
        with open('informacoes.json', 'w', encoding=("Utf-8")) as f:
            json.dump(json_dados, f)
        
        collection_data.insert_one(json_dados)
        del json_dados['_id']
        return HttpResponse(json.dumps(json_dados), content_type="application/json")
    else:
        return HttpResponseForbidden()

@csrf_exempt
def result_response(request):
    with open('informacoes.json', 'r') as f:
        dados = json.load(f)
    return HttpResponse(json.dumps(dados), content_type="application/json")
