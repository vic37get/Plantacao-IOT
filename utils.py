import requests
from bs4 import BeautifulSoup
import re
#geoposition currentconditions forecast

requisiçao = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi'

def temperatura(requisição):
    exp = re.compile("\\<.*?\\>")
    page = requests.get(requisição)
    soup = BeautifulSoup(page.content, 'html.parser')
    temperatura = soup.find_all('span', id='min-temp-1')
    temperatura = re.sub(exp, '', str(temperatura))
    return temperatura
