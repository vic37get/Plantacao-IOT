<h1 align="center"> Plantação IoT: Monitoramento de plantação com ESP8266 🪴  </h1>

## ℹ️ Sobre o projeto
Projeto desenvolvido para a disciplina de Tópicos em **Redes de Computadores**, ministrada pelo professor [Érico Meneses Leão](https://sigaa.ufpi.br/sigaa/public/docente/portal.jsf?siape=2619458), no período de **2022.1** na **Universidade Federal do Piauí (UFPI)**, com objetivo de realizar o monitoramento de parâmetros como umidade do ar, do solo, temperatura, se está ou não chovendo, e também controlar o irrigamento de uma determinada plantação.

## 🔌 Tecnologias
Para o desenvolvimento do projeto foram usadas as seguintes tecnologias:
- [Arduino](https://www.arduino.cc/en/software/): Para programar o dispositivo ESP8266.
- [Django](https://www.djangoproject.com/): Para desenvolvimento do site da aplicação.
- [Heroku](https://dashboard.heroku.com/): para realizar o deploy da aplicação na web.

Além disso, foram usados os seguintes dispositivos:
| Dispositivos                            |
|-----------------------------------------|
| [ESP8266](https://www.filipeflop.com/produto/modulo-wifi-esp8266-nodemcu-esp-12/)                                 |
| [Sensor de chuva](https://www.filipeflop.com/produto/sensor-de-chuva/)                         |
| [Sensor de umidade e temperatura (DHT11)](https://www.filipeflop.com/produto/sensor-de-umidade-e-temperatura-dht11/) |
| [Sensor de umidade do solo](https://www.filipeflop.com/produto/sensor-de-umidade-do-solo-higrometro/)               |

## ▶️ Como instalar e executar
É necessária a instalação de [Python](https://www.python.org/) para execução do projeto. Em seguida, instale as dependências com o seguinte comando:
```
pip install -r requirements.txt
```
E execute o projeto:
```
python3 manage.py runserver
```
---
Para instalar e executar o projeto, deve baixar o *zip* do projeto ou fazer um clone, da seguinte maneira:
```
git clone https://github.com/jhoisz/monitoramento-de-plantacao-com-esp8266
```
Para que o ESP8266 possa ser compilado pelo Arduino IDE, é necessário configurar, você pode acessar o [tutorial](https://www.blogdarobotica.com/2020/05/28/como-programar-a-placa-nodemcu-esp8266-no-arduino-ide/) e realizar esse procedimento.

Em seguida entre na pasta do projeto, abra o projeto com a IDE Arduino e configure o WiFi a qual deseja conectar o seu dispositivo:

```ino
const char* ssid = "loginWiFi"; //login WiFi
const char* password = "senhaWiFi"; //senha WiFi
```
Após isso, apenas conecte seu dispositivo ESP8266 pela USB, selecione a porta COM correta, compile e execute o projeto.

## ✨ Protótipo e funcionalidades do projeto

Você pode acessar o projeto [neste link](http://plantacao.herokuapp.com/). E abaixo você pode acessar as imagens do projeto e do site desenvolvido:

### 💻 Montagem de dispositivos
Foi utilizado o ESP8266 para controle dos sensores e envio de requisições para a API desenvolvida, abaixo uma imagem da disposição destes:
<p align="center">
  <img src="https://github.com/jhoisz/monitoramento-de-plantacao-com-esp8266/blob/main/projeto2.jpeg" style="width: 500px;
  height: auto;" alt= "" />
</p>

### 💡 Funcionalidades da aplicação
A aplicação apresenta uma tela com o status da irrigação (ligado ou desligado), umidade do solo, temperatura, status da chuva (chovendo ou não), previsão do tempo e umidade do ar. Além disso, é possível salvar os registros de cada sensor e visualizá-los em uma página do site. Abaixo um *gif* da aplicação demonstrando seu funcionamento:

<p align="center">
  <img src="https://github.com/jhoisz/monitoramento-de-plantacao-com-esp8266/blob/main/projetoiot.gif" style="width: 800px;
  height: auto;" alt= "" />
</p>

## 🧱 Desafios enfrentados
O desenvolvimento do projeto foi bastante tranquilo, a equipe trabalhou bem. O único impedimento para o funcionamento perfeito do protótipo foi a falta de resistores específicos para o sensor de umidade do solo (Higrômetro), fora isso, nada a contestar.

## 🤝 Desenvolvedores
| [<img src="https://avatars.githubusercontent.com/u/57508736?v=4" width=115><br><sub>Jhoisnáyra Vitória</sub>](https://github.com/jhoisz) |  [<img src="https://avatars.githubusercontent.com/u/51518489?v=4" width=115><br><sub>Victor Ribeiro</sub>](https://github.com/vic37get) |  [<img src="https://avatars.githubusercontent.com/u/60663612?v=4" width=115><br><sub>Marcelo Janio</sub>](https://github.com/MarceloJanio) |
| :---: | :---: | :---: |
