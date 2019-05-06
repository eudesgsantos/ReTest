#include <deprecated.h>
#include <MFRC522.h>
#include <MFRC522Extended.h>
#include <require_cpp11.h>
#include <SPI.h>
#include <LiquidCrystal.h>
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   
LiquidCrystal lcd(6, 7, 5, 4, 3, 2); 

 String lista [3]; //Lista de possíveis opções
 char st[20];
 char serialData = 0;
 int x = 0;
 int estado = 0; //aguardando rfid 1- aguardando report 
 
void setup() 
{
  pinMode(8,INPUT); // Botão "Selecionar"
  pinMode(A0,INPUT); // Botão "Cima"
  pinMode(A1,INPUT); // Botão "Baixo"
  lista[0] = "Ar-condicionado"; //Valores da lista 
  lista[1] = "Luz";
  lista[2] = "Projetor";
  Serial.begin(9600);   // Inicia a serial
  SPI.begin();      // Inicia  SPI bus
  mfrc522.PCD_Init();   // Inicia MFRC522
  Serial.println("Aproxime o seu cartao do leitor...");
  Serial.println();
  //Define o número de colunas e linhas do LCD:  
  lcd.begin(16, 2);
  mensageminicial();
    
}
 
void loop() 
{
  int botao1 = digitalRead(A0); //Cima
  int botao2 = digitalRead(A1); //Baixo
  int bt = digitalRead(8); // Botão select
  String texto = lista[x];

   if (botao1 == HIGH){  
    delay(100);
    if (x < 2){
      x = x + 1 ; 
    }
  }  
  if (botao2 == HIGH){
    delay(100);
    if (x > 0) {
      x = x - 1 ;
      }
     }
  
    if (bt == HIGH){
    Serial.println("YES");
    lcd.clear();
    lcd.print(" Obrigado pelo");
    lcd.setCursor(3,1);
    lcd.print("seu report!");
    delay(3000);
    lcd.clear();
    lcd.setCursor(3,0);
    lcd.print("Verifique");
    lcd.setCursor(4,1);
    lcd.print("seu email!");
    delay(3000);
    mensageminicial();
    
    estado =0;
  } 
   if (bt == LOW){
    Serial.println("NO");
    delay(100);
    }
  
  Serial.println(x);
  if (estado){ //aguardando report
    lcd.clear();
    lcd.print("Seu Report:");
    lcd.setCursor(0,1);
    lcd.print(texto);
    Serial.println(texto);
    
  }  
  else //aguardando rfid
  {
    // Procura novos cartões
    if ( ! mfrc522.PICC_IsNewCardPresent()) 
    {
      Serial.println("New card");
    return;
    }
    // Seleciona um novo cartão
    if ( ! mfrc522.PICC_ReadCardSerial()) 
    {
       Serial.println("Read card");
    return;
    }
    //Mostra UID na serial
    Serial.print("UID da tag :");
    String conteudo= "";
    byte letra;
    for (byte i = 0; i < mfrc522.uid.size; i++) 
    {
       Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
       Serial.print(mfrc522.uid.uidByte[i], HEX);
       conteudo.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
       conteudo.concat(String(mfrc522.uid.uidByte[i], HEX));
    }
    Serial.println();
    Serial.print("Mensagem : ");
    conteudo.toUpperCase();
    if (conteudo.substring(1) == "91 C7 2E 00") //UID 1 - Chaveiro
    {
      Serial.println("Ola Ferraz !");
      Serial.println();
      lcd.clear();
      lcd.print("Ola Ferraz !");
      lcd.setCursor(0,1);
      lcd.print("Acesso liberado!");
      delay(3000);
      lcd.clear();
      lcd.print("Seu Report:");  
      lcd.setCursor(0,1);
      lcd.print(texto);  
    }
   
    if (conteudo.substring(1) == "13 08 B3 02") //UID 2 - Cartao
    {
      Serial.println("Ola Cartao !");
      Serial.println();
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Ola Cartao !");
      lcd.setCursor(0,1);
      lcd.print("Acesso Negado !");
      delay(3000);
      mensageminicial();
      estado = 0;
      return;
      
      
    }
    if (conteudo.substring(1) == "D9 E5 BC 52") //UID 3 - Vem
    {
      Serial.println("Williams está indo!");
      Serial.println();
      lcd.clear();
      lcd.print("Williams chegou!");
      lcd.setCursor(0,1);
      lcd.print("Acesso liberado!");
      delay(3000);
      lcd.clear();
      lcd.print("Seu Report:");  
      lcd.setCursor(0,1);
      lcd.print(texto);  
    }
  }
  Serial.println(x);
  estado = 1;
  

}

 void mensageminicial()
{
  lcd.clear();
  lcd.print(" Aproxime o seu");  
  lcd.setCursor(0,1);
  lcd.print("cartao do leitor");  
 }
