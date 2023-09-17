from machine import Pin, ADC, PWM
from time import sleep

pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)  # seta 12 bits(faixa de 0 - 4095)

led = PWM(Pin(23))


def clamp(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n


def map(leitura):
    tensao = leitura * (3.3 / 4095)
    tensao = clamp(int(tensao * 310), 0, 1023)
    return tensao


while True:
    duty = map(pot.read())
    print(pot.read(), duty)
    led.duty(duty)
    sleep(0.1)
