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
 
//CS, CD, WR, RD, RESET
Adafruit_TFTLCD tft(A3, A2, A1, A0, A4);
int ultimaRefresh; 
int x = 0;
String lista [5]; //Lista de possíveis opções
int botao1;
int botao2;
int bt;
String texto; 
void mudancaTela(void)
{
  texto = lista[x];
  tft.fillRoundRect(5, 150, 312, 50, 5, ORANGE);
  tft.drawRoundRect(5, 150, 312, 50, 5, WHITE);
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
void segundaTela(void)
{
  texto = lista[x];
  tft.fillScreen(BLACK);
  tft.fillRoundRect(5, 15, 312, 100, 5, ORANGE);
  tft.drawRoundRect(5, 15, 312, 100, 5, WHITE);
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
  tft.drawRoundRect(5, 150, 312, 50, 5, WHITE);
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

void verificaBotoes(void){
 botao1 = digitalRead(22); //Cima
 botao2 = digitalRead(23); //Baixo
 bt = digitalRead(24); // Botão select
 Serial.println(botao1);
  if (botao1 == HIGH){  
    delay(100);
    if (x < 4){
      x = x + 1 ; 
    }
    mudancaTela();
  }  
  if (botao2 == HIGH){
    delay(100);
    if (x > 0) {
      x = x - 1 ;
      }
     mudancaTela();   
   }   
  
  Serial.println(x);
  Serial.println(texto);
}

 
void setup(void) 
{
  pinMode(24,INPUT); // Botão "Selecionar"
  pinMode(22,INPUT); // Botão "Cima"
  pinMode(23,INPUT); // Botão "Baixo"
  lista[0] = " Controle      >"; //Valores da lista 
  lista[1] = "<Luz           >";
  lista[2] = "<Projetor      >";
  lista[3] = "<Cadeira       >";
  lista[4] = "<Ar-condicionado";      
  Serial.begin(9600);
  tft.reset();
  delay(500);
  //tft.begin(0x9341) //Use esta linha para o controlador 9341
  tft.begin(0x9325);
  tft.setRotation(3);
  segundaTela();
}
void loop()
{
  //tft.setRotation(3); //Use esta linha para o controlador 9341
  verificaBotoes();
  
  
}

void tela_inicial(uint16_t color)
{
  tft.fillScreen(BLACK);
  tft.fillRoundRect(5, 15, 312, 100, 5, ORANGE);
  tft.drawRoundRect(5, 15, 312, 100, 5, WHITE);
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(13, 31);
  tft.println("  Aproxime seu ");
  tft.setCursor(13, 71);
  tft.println("cartao do leitor");
  tft.setTextColor(BLACK);
  tft.setTextSize(3);
  tft.setCursor(14, 32);
  tft.println("  Aproxime seu ");
  tft.setCursor(14, 72);
  tft.println("cartao do leitor");
  tft.setTextColor(WHITE);
  tft.setTextSize(3);
  tft.setCursor(15, 30);
  tft.println("  Aproxime seu ");
  tft.setCursor(15, 70);
  tft.println("cartao do leitor");
  delay(30000);
}

void tela_reporte(uint16_t color)
{
 botao1 = digitalRead(22); //Cima
 botao2 = digitalRead(23); //Baixo
 bt = digitalRead(24); // Botão select
 Serial.println(botao1);
    
}
