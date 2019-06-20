#include <SoftwareSerial.h>
#include <RDM6300.h>
#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_TFTLCD.h> // Hardware-specific library
 
//Definicao de cores
#define BLACK           0x0000
#define BLUE            0x001F
#define RED             0xF800
#define GREEN           0x07E0
#define CYAN            0x07FF
#define MAGENTA         0xF81F
#define YELLOW          0xFFE0
#define WHITE           0xFFFF
#define ORANGE          0xFBE0

SoftwareSerial RFID(50,18);
uint8_t Payload[6];
RDM6300 RDM6300(Payload);

Adafruit_TFTLCD tft(A3, A2, A1, A0, A4);

const int ledPin = 50;
int ledState = LOW;    
unsigned long tempreset = 0;  
const long interval = 120000;
const long intervalled = 3000;
int b = 0;
int a = 0;
int y = 0;
int x = 1;
int z = 0;
String listaR [6][6] = {
  {"", " Controle      >", "<Luz           >", "<Projetor      >", "<Cadeira       >", "<Ar-condicionado"}, //Valores da lista 
  {"", "Faltando       >", "<Quebrado      >", "<Sem bateria    "},
  {"", "Piscando       >", "<Sem ligar       "},
  {"", "Sem ligar      >", "<Quebrado      >", "<Sem bateria    "},
  {"", "Quebrada       >", "<Faltando       "},
  {"", "Pingando       >", "<Sem esfriar   >", "<Quebrado       "},};
int btb;
int botao1;
int botao2;
int bt;
String texto;

void(* resetFunc) (void) = 0;

void RDM3600 (void)
{ 
  //Aguarda a aproximacao da tag RFID
  if (RFID.available() > 0) {
    uint8_t c = RFID.read();
    if (RDM6300.decode(c)){
      digitalWrite(52,HIGH);
      segundaTela();
      b = b + 1;
      tempreset = millis();
      //Mostra os dados no serial monitor
      for (int i = 0; i < 5; i++)      {
        Serial.print(Payload[i], HEX);
        Serial.print(" ");
      }
    }
  }
 }

void telainicial(void)
{
  tft.fillScreen(WHITE);
  tft.fillRoundRect(5, 15, 312, 100, 5, ORANGE);
  tft.drawRoundRect(5, 15, 312, 100, 5, BLACK);
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(13, 31);
  tft.println("  Aproxime seu ");
  tft.setCursor(15, 71);
  tft.println("cracha do leitor");
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(13, 32);
  tft.println("  Aproxime seu ");
  tft.setCursor(16, 72);
  tft.println("cracha do leitor");
  tft.setTextColor(WHITE);
  tft.setTextSize(3);
  tft.setCursor(15, 30);
  tft.println("  Aproxime seu ");
  tft.setCursor(17, 70);
  tft.println("cracha do leitor");
  tft.drawLine(116,69,121,64,BLACK);
  tft.drawLine(114,71,119,66,BLACK); 
  tft.drawLine(116,71,121,66,BLACK);
  tft.drawLine(115,71,120,66,BLACK);
  tft.drawLine(116,70,121,65,BLACK);
  tft.drawLine(115,70,120,65,WHITE);
  tft.drawLine(114,70,119,65,WHITE);
  tft.drawLine(115,69,120,64,WHITE);
  tft.drawLine(114,69,119,64,WHITE);
}

void segundaTela(void)
{
  texto = listaR[y][x];
  tft.fillScreen(WHITE);
  tft.fillRoundRect(5, 15, 312, 100, 5, ORANGE);
  tft.drawRoundRect(5, 15, 312, 100, 5, BLACK);
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(18, 31);
  tft.println(" Selecione seu ");
  tft.setCursor(18, 71);
  tft.println("    Report");
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(19, 32);
  tft.println(" Selecione seu ");
  tft.setCursor(19, 72);
  tft.println("    Report");
  tft.setTextColor(WHITE);
  tft.setTextSize(3);
  tft.setCursor(20, 30);
  tft.println(" Selecione seu ");
  tft.setCursor(20, 70);
  tft.println("    Report");
  tft.fillRoundRect(5, 150, 312, 50, 5, ORANGE);
  tft.drawRoundRect(5, 150, 312, 50, 5, BLACK);
  tft.setCursor(16,163);
  tft.setTextColor(BLACK);
  tft.println(texto);
  tft.setTextColor(BLACK);
  tft.setCursor(17,164);
  tft.println(texto);
  tft.setTextColor(WHITE);
  tft.setCursor(18,165);
  tft.println(texto);
}

void terceiratela(void)
{ 
  texto = listaR [y][x];
   digitalWrite(52,LOW);
  tft.fillScreen(WHITE);
  tft.fillRoundRect(5, 15, 312, 100, 5, ORANGE);
  tft.drawRoundRect(5, 15, 312, 100, 5, BLACK);
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(18, 31);
  tft.println("Especifique seu ");
  tft.setCursor(18, 71);
  tft.println("    Report");
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(19, 32);
  tft.println("Especifique seu ");
  tft.setCursor(19, 72);
  tft.println("    Report");
  tft.setTextColor(WHITE);
  tft.setTextSize(3);
  tft.setCursor(20, 30);
  tft.println("Especifique seu ");
  tft.setCursor(20, 70);
  tft.println("    Report");
  tft.fillRoundRect(5, 150, 312, 50, 5, ORANGE);
  tft.drawRoundRect(5, 150, 312, 50, 5, BLACK);
  tft.setCursor(16,163);
  tft.setTextColor(BLACK);
  tft.println(texto);
  tft.setTextColor(BLACK);
  tft.setCursor(17,164);
  tft.println(texto);
  tft.setTextColor(WHITE);
  tft.setCursor(18,165);
  tft.println(texto); 
  a = a + 1;
  }
void telafinal(void)
{
  tft.fillScreen(WHITE);
  tft.fillRoundRect(40, 15, 215, 55, 5, ORANGE);
  tft.drawRoundRect(40, 15, 215, 55, 5, BLACK);
  tft.setTextColor(BLACK);
  tft.setCursor(13, 31);
  tft.println("   Obrigado!");
  tft.setTextColor(BLACK);
  tft.setCursor(14, 32);
  tft.println("   Obrigado!");
  tft.setTextColor(WHITE);
  tft.setCursor(15, 30);
  tft.println("   Obrigado!");
  tft.fillRoundRect(5, 80, 312, 150, 5, ORANGE);
  tft.drawRoundRect(5, 80, 312, 150, 5, BLACK);
  tft.setTextColor(BLACK);
  tft.setCursor(13, 90);
  tft.println("Verifique no seu");
  tft.setCursor(14, 89);
  tft.println("Verifique no seu");
  tft.setTextColor(WHITE);
  tft.setCursor(15, 88);
  tft.println("Verifique no seu");
  tft.setTextColor(BLACK);
  tft.setCursor(13, 126);
  tft.println("    e-mail,");
  tft.setCursor(14, 125);
  tft.println("    e-mail,");
  tft.setTextColor(WHITE);
  tft.setCursor(15, 124);
  tft.println("    e-mail,");
  tft.setTextColor(BLACK);
  tft.setCursor(13, 162);
  tft.println(" o andamento do");
  tft.setCursor(14, 161);
  tft.println(" o andamento do");
  tft.setTextColor(WHITE);
  tft.setCursor(15, 160);
  tft.println(" o andamento do");
  tft.setTextColor(BLACK);
  tft.setCursor(13, 198);
  tft.println("    reporte");
  tft.setCursor(14, 197);
  tft.println("    reporte");
  tft.setTextColor(WHITE);
  tft.setCursor(15, 196);
  tft.println("    reporte");
  delay(5000)
 ziu resetFunc();

}
  

void mudancaTela(void)
{
  texto = listaR[y][x];
  tft.fillRoundRect(5, 150, 312, 50, 5, ORANGE);
  tft.drawRoundRect(5, 150, 312, 50, 5, BLACK);
  tft.setCursor(16,163);
  tft.setTextColor(BLACK);
  tft.println(texto);
  tft.setTextColor(BLACK);
  tft.setCursor(17,164);
  tft.println(texto);
  tft.setTextColor(WHITE);
  tft.setCursor(18,165);
  tft.println(texto);
}

void verificaBotoes(void)
{
 btb = digitalRead(31); //Back
 bt = digitalRead(29); //Select
 botao1 = digitalRead(28); //Cima
 botao2 = digitalRead(30); //Baixo
  if (botao1 == LOW){  
    delay(150);
    if (a == 1 or a == 0){
     if (y == 1 and x < 3){
      x = x + 1;
      mudancaTela();
     }
     if (y == 2 and x < 2){
      x = x + 1;
      mudancaTela();
     }
     if (y == 3 and x < 3){
      x = x + 1;
      mudancaTela();
     }
     if (y == 4 and x < 2){
      x = x + 1;
      mudancaTela();
     }
     if (y == 5 and x < 3){
      x = x + 1;
      mudancaTela();
     }
     if (y == 0 and x < 5){
      x = x + 1 ; 
      mudancaTela();
     }
    } 
  }  
  if (botao2 == LOW){
    delay(150);
    if (a == 1 or a == 0){
     if (x > 1) {
      x = x - 1 ;
      mudancaTela();   
     }
    }
   } 
   if (bt == LOW){
     if (a == 1){
      Serial.println("");
      Serial.println(listaR[0][z]);
      Serial.println(texto);
      Serial.end();
      telafinal();
     }
     if (a == 0){
       delay(150);
       z = x;
       y = x;
       x = 1;
       terceiratela();
     }
   }
    if (btb == LOW){
     if (a == 1){
      Serial.println("passsou");
      a = 0;
      x = 1;
      y = 0;
      segundaTela();
      }
     }
}

 
void setup(void) 
{
  Serial.begin(9600);
  RFID.begin(9600);
  pinMode(52,OUTPUT);// LED
  pinMode(31,INPUT); // Botão "Voltar"
  pinMode(29,INPUT); // Botão "Selecionar"
  pinMode(28,INPUT); // Botão "Cima"
  pinMode(30,INPUT); // Botão "Baixo"
  tft.reset();
  tft.begin(0x9325);
  tft.setRotation(1);
  telainicial();
}
void loop()
{ 
  if (b == 0){
    RDM3600();
  }
  
  if (b == 1){
     verificaBotoes();
     if ((millis() - tempreset) > intervalled){
      digitalWrite(52,HIGH);
     }
     
     if ((millis() - tempreset) > interval){
        resetFunc();
     }
  }
}
  
