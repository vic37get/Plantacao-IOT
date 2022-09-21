import requests
from bs4 import BeautifulSoup
import re
#geoposition currentconditions forecast

API_KEY=''
def previsão_tempo():
    exp = re.compile("\\<.*?\\>")
    page = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi")
    soup = BeautifulSoup(page.content, 'html.parser')
    temperatura = soup.find_all('span', id='min-temp-1')
    temperatura = re.sub(exp, '', temperatura)
    print(temperatura)
    return

