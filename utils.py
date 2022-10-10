import re

import requests
from bs4 import BeautifulSoup
#from pymongo import MongoClient

#def connectMongo(db_name):
#    client = MongoClient('mongodb+srv://vic35get:005EFsVTBrldkZpp@plantacaoiot.fc1r2gv.mongodb.net/?retryWrites=true&w=majority&socketTimeoutMS=360000&connectTimeoutMS=360000')
#    db = client[db_name]
#    return db

def temperaturaMinima():
    request = "https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi"
    exp = re.compile("\\<.*?\\>")
    page = requests.get(request)
    soup = BeautifulSoup(page.content, 'html.parser')
    temperatura = soup.find_all('span', id='min-temp-1')
    temperatura = re.sub(exp, '', str(temperatura))
    temperatura = temperatura[1:4]
    return temperatura

def temperaturaMaxima():
    request = "https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi"
    exp = re.compile("\\<.*?\\>")
    page = requests.get(request)
    soup = BeautifulSoup(page.content, 'html.parser')
    temperatura_maxima = soup.find_all('span', id='max-temp-1')
    temperatura_maxima = re.sub(exp, '', str(temperatura_maxima[0]))
    return temperatura_maxima

def umidadeMinima():
    request = "https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi"
    exp = re.compile("\\<.*?\\>")
    page = requests.get(request)
    soup = BeautifulSoup(page.content, 'html.parser')
    umidade_minima = soup.find_all('span', class_='-gray-light')
    umidade_minima = re.sub(exp, '', str(umidade_minima[2]))
    return umidade_minima

def umidadeMaxima():
    request = "https://www.climatempo.com.br/previsao-do-tempo/cidade/264/teresina-pi"
    exp = re.compile("\\<.*?\\>")
    page = requests.get(request)
    soup = BeautifulSoup(page.content, 'html.parser')
    umidade_maxima = soup.find_all('span', class_='-gray-light')
    umidade_maxima = re.sub(exp, '', str(umidade_maxima[3]))
    return umidade_maxima
