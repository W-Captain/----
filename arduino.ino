#include<LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int buttom=8;
int servopin=9;//设置舵机驱动脚到数字口9
int myangle;//定义角度变量
int pulsewidth;//定义脉宽变量
void servopulse(int servopin,int myangle)/*定义一个脉冲函数，用来模拟方式产生PWM值*/
{
  pulsewidth=(myangle*11)+500;//将角度转化为500-2480 的脉宽值
  digitalWrite(servopin,HIGH);//将舵机接口电平置高
  delayMicroseconds(pulsewidth);//延时脉宽值的微秒数
  digitalWrite(servopin,LOW);//将舵机接口电平置低
  delay(20-pulsewidth/1000);//延时周期内剩余时间
}
void duoji(char val)
{
  if(val>'0'&&val<='9')//判断收到数据值是否符合范围
  {
    val=val-'0';//将ASCII码转换成数值，例'9'-'0'=0x39-0x30=9
    val=val*(180/9);//将数字转化为角度，例9*（180/9）=180
    Serial.print("moving servo to ");
    Serial.print(val,DEC);
    Serial.println();
    for(int i=0;i<=50;i++) //产生PWM个数，等效延时以保证能转到响应角度
    {
      servopulse(servopin,val);//模拟产生PWM
    }
  }
}
void setup()
{
  lcd.begin(16, 2);
  pinMode(servopin,OUTPUT);//设定舵机接口为输出接口
  Serial.begin(9600);//设置波特率为9600
  Serial.println("servo=o_seral_simple ready" ) ;
  pinMode(buttom,INPUT);
}
int temp[4];
int j=1;
void loop()
{
  while(j)
  {
    Serial.println("test");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Locked!!");
    delay(200);
    temp[0]=Serial.read();
    temp[1]=Serial.read();
    temp[2]=Serial.read();
    temp[3]=Serial.read();
    if(temp[0]=='k'&&temp[1]=='u'&&temp[2]=='a'&&temp[3]=='n')
    {
      j=0;
      break;
    }
  }
  int xx=analogRead(A0);
  int yy=analogRead(A1);
  int judge=digitalRead(buttom);
  int tempj=0;
  tempj=Serial.read();
  if(judge!=1 | tempj>1)
  {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("OK");
    duoji('1');
    //tempj=0;
    judge =1;
    Serial.print(tempj);
  }
  //duoji('5');
  //Serial.print(dis); 
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("(");
  lcd.print(xx);
  lcd.print(",");
  lcd.print(yy);
  lcd.print(")");
  lcd.setCursor(0, 1);
  lcd.print(judge);
  delay(200);
} 
