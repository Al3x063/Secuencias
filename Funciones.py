from machine import Pin
from time import sleep, sleep_ms

pulsador=Pin(32,Pin.IN)
pulsador1=Pin(35,Pin.IN)
pulsador2=Pin(19,Pin.IN)
pulsador3=Pin(23,Pin.IN,Pin.PULL_UP)
pulsador4=Pin(1,Pin.IN,Pin.PULL_UP)
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
leds2 = [led2,led1,led4, led3, led6, led5,led8,led7,led10,led9]
leds3 = [led9,led3,led2,led10,led1,led8,led5,led4,led6,led7]
leds4= [led2,led4,led6,led8,led10]
leds5 = [led1,led3,led5,led7,led9]
leds6=[led2,led6,led10,led9,led1,led7,led5]

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
        led5.value(1)
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
    for i in range(2):
        led1.value(1)
        sleep_ms(100)
        led10.value(1)
        sleep_ms(100)
        led1.value(0)
        led10.value(0)
        led2.value(1)
        sleep_ms(100)
        led9.value(1)
        sleep_ms(100)
        led2.value(0)
        led9.value(0)
        led3.value(1)
        sleep_ms(100)
        led8.value(1)
        sleep_ms(100)
        led3.value(0)
        led8.value(0)
        led4.value(1)
        sleep_ms(100)
        led7.value(1)
        sleep_ms(100)
        led4.value(0)
        led7.value(0)
        led5.value(1)
        sleep_ms(100)
        led6.value(1)
        sleep_ms(100)
        led5.value(0)
        led6.value(0)
def secuencia5():
    for i in range (2):
        led5.value(1)
        sleep_ms(100)
        led6.value(1)
        sleep_ms(100)
        led5.value(0)
        led6.value(0)
        led4.value(1)
        sleep_ms(100)
        led7.value(1)
        sleep_ms(100)
        led4.value(0)
        led7.value(0)
        led3.value(1)
        sleep_ms(100)
        led8.value(1)
        sleep_ms(100)
        led3.value(0)
        led8.value(0)
        led2.value(1)
        sleep_ms(100)
        led9.value(1)
        sleep_ms(100)
        led2.value(0)
        led9.value(0)
        led1.value(1)
        sleep_ms(100)
        led10.value(1)
        sleep_ms(100)
        led1.value(0)
        led10.value(0)
def secuencia6():
    for i in leds2:
        i.value(1)
        sleep(0.5)
        i.value(3)
        sleep(0.05)
        i.value(1)
        for j in reversed (leds2):
            i.value(0)
            sleep(0.5)
            i.value(3)
            sleep(0.05)
            i.value(1)
def secuencia7():
    for i in leds3:
        i.value(1)
        sleep(0.5)
        i.value(3)
        sleep(0.05)
        i.value(1)
def secuencia8(): 
    for i in leds4:
        i.value(1)
        sleep(0.5)
        i.value(3)
        sleep(0.05)
        i.value(1)
    for j in leds5:
        j.value(1)
        sleep(0.5)
        j.value(3)
        sleep(0.05)
        j.value(1)
def secuencia9():
    for i in leds5:
        i.value(1)
        sleep(0.5)
        i.value(3)
        sleep(0.05)
        i.value(1)      
while True:
    if pulsador.value():
        secuencia1()
    if pulsador1.value():
        secuencia2()
    if pulsador2.value():
        secuencia3() 
    if not pulsador3.value():
        secuencia4()
    if (pulsador.value() and  not pulsador3.value()):
        secuencia5()
    if (pulsador.value() and pulsador1.value()):
        secuencia6()
    if (pulsador.value() and pulsador2.value()):
        secuencia7()
    if (pulsador3.value() and pulsador2.value()): 
        secuencia8()
    if not pulsador4.value():
        secuencia9()
    
    
