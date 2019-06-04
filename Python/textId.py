import serial
import time

Arduinoserial = serial.Serial('COM14')

strokes = []

while True:
    res = Arduinoserial = serial.Serial('COM14')
    if res not in strokes:
        res = res.replace("'",'')
        res = res.replace("  ",'')
        res = res.replace("\n",'')
        res = res.replace("<",'')
        res = res.replace(">",'')
        res = res.replace("\r",'')
        strokes.append(res)
    print(strokes)
