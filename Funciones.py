from machine import Pin
from time import sleep, sleep_ms

pulsador=Pin(32,Pin.IN)
pulsador1=Pin(35,Pin.IN)
pulsador2=Pin(19,Pin.IN)
pulsador3=Pin(23,Pin.IN,Pin.PULL_UP)
led1=Pin(33,Pin.OUT)
led2=Pin(12,Pin.OUT)
led3=Pin(27,Pin.OUT)
led4=Pin(14,Pin.OUT)
led5=Pin(25,Pin.OUT)
led6=Pin(2,Pin.OUT)
led7=Pin(4,Pin.OUT)
led8=Pin(16,Pin.OUT)
led9=Pin(5,Pin.OUT)
led10=Pin(3,Pin.OUT)

leds = [led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]

def secuencia1():
  for i in leds:
      i.value(1)
      sleep_ms(50)
      i.value(0)
      sleep(0.05)
def secuencia2():
    for i in reversed (leds):
        for j in range(2):
            i.value(1)
            sleep_ms(50)
            i.value(0)
            sleep(0.05)
def secuencia3():
    for i in range(2):  
        led1.value(1)
        led2.value(1)
        led3.value(1)
        led4.value(1)
        led4.value(1)
        sleep_ms(50)
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        sleep_ms(100)
        for j in range (2):
            led6.value(1)
            led7.value(1)
            led8.value(1)
            led9.value(1)
            led10.value(1)
            sleep_ms(50)
            led6.value(0)
            led7.value(0)
            led8.value(0)
            led9.value(0)
            led10.value(0)
            sleep_ms(100)
def secuencia4():
    for i in leds:
        for n in range(3):
            n=0
            if n==0:
                led1.value(1)
                led9.value(1)
                led2.value(1)
                led9.value(1)
                led3.value(1) 
            elif n==1:
                led2.value(1)
                led8.value(1)
                led2.value(0)
                led7.value(0)
            elif n==2:
                led3.value(1)
                led7.value(1)
                led1.value(0)
                led6.value(0)
            elif n==3:
                led4.value(1)
                led6.value(1)
                led2.value(0)
                led5.value(0)
while True:
    if pulsador.value():
        secuencia1()
    if pulsador1.value():
        secuencia2()
    if pulsador2.value():
        secuencia3() 
    if not pulsador3.value():
        secuencia4() 
    
    