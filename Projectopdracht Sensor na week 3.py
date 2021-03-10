#https://canvas.kdg.be/courses/23181/assignments/70984
from machine import UART

uart = UART(1)
uart.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=190)

while True:
    header_bytes = uart.read(1)
    data_header = int(uart.read(1)[0])
    data_high = int(uart.read(2)[0])
    data_low = int(uart.read(3)[0])
    distance = data_high*256 + data_low
    if int(distance/10) < 1000:
        print("Distance",int(distance/10), "centimeter")
