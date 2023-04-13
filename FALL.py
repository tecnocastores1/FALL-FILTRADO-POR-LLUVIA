import machine
from machine  import Pin
from hcs404 import HCSR04
from time import sleep
from machine import Pin, ADC
import time

# Ultrasonico
sensor1 = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
sensor2 = HCSR04(trigger_pin=17, echo_pin=16, echo_timeout_us=10000)
sensor3 = HCSR04(trigger_pin=2, echo_pin=15, echo_timeout_us=10000)
sensor4 = HCSR04(trigger_pin=26, echo_pin=25, echo_timeout_us=10000)

#Sensor de luvia
rain_analog1 = 34 
rain_digital1 = 23
rain_analog2 = 35
rain_digital2 = 22
rain_analog3 = 32
rain_digital3 = 21
rain_analog4 = 33
rain_digital4 = 19

adc1 = ADC(Pin(rain_analog1))
adc1.atten(ADC.ATTN_11DB)
adc2 = ADC(Pin(rain_analog2))
adc2.atten(ADC.ATTN_11DB)
adc3 = ADC(Pin(rain_analog3))
adc3.atten(ADC.ATTN_11DB)
adc4 = ADC(Pin(rain_analog3))
adc4.atten(ADC.ATTN_11DB)

rain_digital_pin1 = Pin(rain_digital1, Pin.IN)
rain_digital_pin2 = Pin(rain_digital2, Pin.IN)
rain_digital_pin3 = Pin(rain_digital3, Pin.IN)
rain_digital_pin4 = Pin(rain_digital4, Pin.IN)

#Actuador
Led1 = machine.Pin(12, machine.Pin.OUT)
Led2 = machine.Pin(13, machine.Pin.OUT)
Led3 = machine.Pin(4, machine.Pin.OUT)
Led4 = machine.Pin(27, machine.Pin.OUT)

while True:
    contenedor1 = sensor1.distance_cm()
    contenedor2 = sensor2.distance_cm()
    contenedor3 = sensor3.distance_cm()
    contenedor4 = sensor4.distance_cm()
    
    print('Distancia1: ', contenedor1, 'cm')
    print('Distancia2: ', contenedor2, 'cm')
    print('Distancia3: ', contenedor3, 'cm')
    print('Distancia4: ', contenedor4, 'cm')
    sleep(2)
    
    rain_analog_val1 = adc1.read()
    rain_digital_val1 = rain_digital_pin1.value()
    rain_analog_val2 = adc2.read()
    rain_digital_val2 = rain_digital_pin2.value()
    rain_analog_val3 = adc3.read()
    rain_digital_val3 = rain_digital_pin3.value()
    rain_analog_val4 = adc4.read()
    rain_digital_val4 = rain_digital_pin4.value()
    
    print('Sensor 1:')
    print(rain_analog_val1, end='')
    print('t', end='')
    print(rain_digital_val1)
    
    print('Sensor 2:')
    print(rain_analog_val2, end='')
    print('t', end='')
    print(rain_digital_val2)
    
    print('Sensor 3:')
    print(rain_analog_val3, end='')
    print('t', end='')
    print(rain_digital_val3)
    
    print('Sensor 4:')
    print(rain_analog_val4, end='')
    print('t', end='')
    print(rain_digital_val4)
    
    #1 = servo encnendido
    #0 = sevo a a 0° grados
    
    #1 no esta lloviendo
    #0 si llueve
    if(contenedor1 <= 13 and contenedor1>=0):
        Led1.value(0)
        if(rain_digital_val1 == 1 and rain_digital_val2 == 1 and rain_digital_val3 == 1 and rain_digital_val4 ==1)
        Led1.value(0)
        else
        Led1.value(1)
    else:
        Led1.value(1)
        
    if(contenedor2 <= 10 and contenedor2>=0):
        Led2.value(1)
    else:
        Led2.value(0)
    
    if(contenedor3 <= 10 and contenedor3>=0):
        Led3.value(1)
    else:
        Led3.value(0)

    if(contenedor4 <= 10 and contenedor4>=0):
        Led4.value(1)
    else:
        Led4.value(0)
