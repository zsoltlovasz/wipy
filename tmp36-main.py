import machine
import socket

adc=machine.ADC()
temppin=adc.channel(pin='GP3')

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
s.bind(('192.168.1.4',11111))
s.listen(1)

while True:
    cli_s,cli_a=s.accept()
    cli_s.sendall(str(temppin())+"\n")
    cli_s.close()
