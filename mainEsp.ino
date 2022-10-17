#include "DHT.h" // Biblioteca DHT
 
#define DHTPIN 18 // Pino do DHT
#define DHTTYPE DHT11 // DHT 11

#include <WiFi.h> // Biblioteca de WiFi
#include <HTTPClient.h> // Biblioteca de HTTP

#define LED_ON 19

#define CHUVAPIN 21

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "ERRO"; //login WiFi
const char* password = "20199030779"; //senha WiFi

int chuva = 0;

String statusIrrigacao = "1";

void setup() {
  Serial.begin(115200);

  pinMode(CHUVAPIN, INPUT);
  pinMode(LED_ON, OUTPUT);
//  pinMode(LED_OFF, OUTPUT);
  
  dht.begin(); //inicializaçao do sensor DHT

  WiFi.begin(ssid, password); //inicialização do WiFi

  Serial.println("Conectando ao WiFi...");
  while (WiFi.status() != WL_CONNECTED) { // Verificação de conexão
    delay(1000);
    Serial.println("...");
  }

  ligaLed(LED_ON);
  Serial.println("Conectado a rede WiFi!");
  Serial.println("-------------------------------------------------------------");
}

void loop() {

  chuva = digitalRead(CHUVAPIN);
  
  //obtem valores de umidade e temperatura
  float umidade = dht.readHumidity();
  float temperatura = dht.readTemperature();

  if (isnan(temperatura) || isnan(umidade)){ //verifica se o valor de DHT é válido
    Serial.println("Esperando um valor valido...");
  }else{
    imprimeDht(umidade, temperatura);
    imprimeSensorChuva(chuva);
    if(WiFi.status()==WL_CONNECTED){ //Verifica se o WiFi está conectado
      realizaRequisicaoPost(umidade, temperatura, chuva);
    }else{
      desligaLed(LED_ON);
      Serial.println("Erro na conexão WiFi :(");   
    }
  }
  delay(10000);  //Aguarda 10 segundos  
}


//void piscaLed(){
//    digitalWrite(LED_OFF, HIGH);
//    delay(1000);
//    digitalWrite(LED_OFF, LOW);
//    delay(1000);
//}

void desligaLed(int led){
  digitalWrite(led, LOW);
}

void ligaLed(int led){
  digitalWrite(led, HIGH);
}

void imprimeDht(float umidade, float temperatura){
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" *C");
    Serial.print("Umidade: ");
    Serial.print(umidade);
    Serial.print(" %t");
}

void imprimeSensorChuva(int sensorChuva){
  Serial.print("\nSensor de Chuva: ");
  Serial.println(sensorChuva);
}

void realizaRequisicaoPost(float umidade, float temperatura, int sensorChuva){
   HTTPClient http;   
   String urlPrincipal = "https://plantacao.herokuapp.com/info?";
   String url = urlPrincipal + "temperatura=" + (String)temperatura+ "&chuva="+(String)sensorChuva+ "&status="+ statusIrrigacao + "&umidadeAr=" +(String)umidade + "&umidadeSolo=80";

    Serial.println(url);
   
   http.begin(url);  //Especifica rota de requisicao
   http.addHeader("Content-Type", "multipart/form-data"); //Especifica o cabecalho
  
   int httpResponseCode = http.POST("");   //Envia uma requisicao POST
  
   if(httpResponseCode>0){ //Verifica codigo RESPONSE
      //Respostas de informação (100-199),
      //Respostas de sucesso (200-299),
      //Redirecionamentos (300-399)
      //Erros do cliente (400-499)
      //Erros do servidor (500-599).
    String response = http.getString(); // Recebe o retorno da requisicao

    Serial.println("\n-------------------------------------------------------------");
    Serial.println("HTTP Response Code:"+(String)httpResponseCode);
    Serial.println("Response: "+response);     
   }else{
    Serial.print("Erro na requisicao: ");
    Serial.println(httpResponseCode);
   }
   http.end(); 
}