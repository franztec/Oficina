from machine import Pin, PWM
from time import sleep

led = PWM(Pin(23))

while True:
    for i in range(0, 1023, 5):
        led.duty(i)
        sleep(0.01)
    for i in range(1023, 0, -5):
        led.duty(i)
        sleep(0.01)
    sleep(0.1)
