#!/usr/bin/python
#
# 20190404 DAF Prende y apaga pines 
#
# Usar: python lape.py NroPin Accion
#       python lape.py 3 on 
#       python lape.py 3 off
#
# PIN -> OPTO
#  2      VCC
#  6      GND      
#  3      IN1
#  5      IN2
#  7      IN3
# 11      IN4
# 13      IN5
# 15      IN6
# 19      IN7
# 21      IN8


import RPi.GPIO as GPIO
import sys

ppin= int(sys.argv[1])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(ppin,GPIO.OUT,initial=0)

try:
    if sys.argv[2]=="on":
        print("ON")
        GPIO.output(ppin,GPIO.LOW)
    elif sys.argv[2]=="off":
        print("OFF")
        GPIO.output(ppin,GPIO.HIGH)
finally:
    print("OK")
