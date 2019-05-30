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
  {"", "Pingando       >", "<Sem esfriar   >", "<Quebrado       "},
};
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
    if (RDM6300.decode(c))    {
      Serial.println("ID TAG: ");
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
  tft.fillRoundRect(5, 15, 312, 100, 5, ORANGE);
  tft.drawRoundRect(5, 15, 312, 100, 5, BLACK);
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(13, 31);
  tft.println("  Obrigado pelo ");
  tft.setCursor(13, 71);
  tft.println("   seu report");
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(14, 32);
  tft.println("  Obrigado pelo ");
  tft.setCursor(14, 72);
  tft.println("   seu report");
  tft.setTextColor(WHITE);
  tft.setTextSize(3);
  tft.setCursor(15, 30);
  tft.println("  Obrigado pelo ");
  tft.setCursor(15, 70);
  tft.println("   seu report");
  tft.fillRoundRect(5, 150, 312, 85, 5, ORANGE);
  tft.drawRoundRect(5, 150, 312, 85, 5, BLACK);
  tft.setCursor(21, 165);
  tft.setTextColor(BLACK);
  tft.println(" Verifique seu ");
  tft.setTextColor(BLACK);
  tft.setCursor(22, 164);
  tft.println(" Verifique seu ");
  tft.setTextColor(WHITE);
  tft.setCursor(23, 163);
  tft.println(" Verifique seu ");
  tft.setTextColor(BLACK);
  tft.setCursor(13, 205);
  tft.println("     e-mail ");
  tft.setCursor(14, 204);
  tft.println("     e-mail ");
  tft.setTextColor(WHITE);
  tft.setCursor(15, 203);
  tft.println("     e-mail ");
  delay(5000);    
  resetFunc();
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
 btb = digitalRead(25); //Back
 bt = digitalRead(24); //Select
 botao1 = digitalRead(22); //Cima
 botao2 = digitalRead(23); //Baixo
  if (botao1 == HIGH){  
    delay(100);
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
  if (botao2 == HIGH){
    delay(100);
    if (a == 1 or a == 0){
     if (x > 1) {
      x = x - 1 ;
      mudancaTela();   
     }
    }
   } 
   if (bt == HIGH){
     if (a == 1){
      Serial.println(listaR[0][z]);
      Serial.println(texto);
      Serial.end();
      telafinal();
     }
     if (a == 0){
       delay(100);
       z = x;
       y = x;
       x = 1;
       terceiratela();
     }
   }
    if (btb == HIGH){
     if (a == 1){
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
  pinMode(25,INPUT); // Botão "Voltar"
  pinMode(24,INPUT); // Botão "Selecionar"
  pinMode(22,INPUT); // Botão "Cima"
  pinMode(23,INPUT); // Botão "Baixo"
  tft.reset();
  tft.begin(0x9325);
  tft.setRotation(3);
  telainicial();
}
void loop()
{
  verificaBotoes();  
}
  
