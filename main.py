import time
from machine import Pin
from machine import rng
from ws2812 import WS2812


p_r1=Pin('GP0', mode=Pin.OUT)
p_r2=Pin('GP9', mode=Pin.OUT)
p_y1=Pin('GP8', mode=Pin.OUT)
p_t1=Pin('GP1', mode=Pin.OUT)
p_g1=Pin('GP2', mode=Pin.OUT)
chain = WS2812(spi_bus=0, led_count=12, intensity_divider=8)
#data=[(machine.rng()%16*(i%3), machine.rng()%16*((i+1)%3), machine.rng()%16*((i+2)%3)) for i in range(12)]
#raibow colours here
data=[(255, 0, 0) ,(255, 127, 0) ,(255, 255, 0) ,(0, 255, 0) ,(0, 0, 255) ,(46, 43, 95) ,(139, 0, 255), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)  ]


def blink(p, s=100):
    p.value(1)
    time.sleep_ms(s)
    p.value(0)
    time.sleep_ms(s)

while True:
    blink(p_r1)
    blink(p_t1)
    blink(p_r2)
    blink(p_t1)
    blink(p_y1)
    blink(p_t1)
    blink(p_g1)
    blink(p_t1)
    chain.show(data)
    tmp=data[0]
    for i in range(11):
        data[i]=data[i+1]
    data[11]=tmp
    time.sleep_ms(5000)

