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
 
void setup(void) 
{
  Serial.begin(9600);
  Serial.println("Teste de LCD 8 Bits");
  tft.reset();
  delay(500);
  //tft.begin(0x9341) //Use esta linha para o controlador 9341
  tft.begin(0x9325);
}
void loop()
{
  //tft.setRotation(3); //Use esta linha para o controlador 9341
  tft.setRotation(1);
  teste_texto(RED); 
}

void teste_texto(uint16_t color)
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
