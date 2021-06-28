# -*- coding: utf-8 -*-
"""
Raspberry pi

2 - SEVEN SEGMENT PROGRAM
"""
import RPi.GPIO as GPIO             #include GPIO library 
import time                         #include time delay library
GPIO.cleanup()                      #initially to reset all GPIO pins

GPIO.setmode(GPIO.BOARD)
chan_list = [3,5,7,11,13,15,19,21]  #8 bits (Bit 0 is 21(LSB), Bit 7 is 3(MSB))
ctrl_pins=[12,16]                   # Control pins 16->1st segment, 12->2nd segment
GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(ctrl_pins, GPIO.OUT)

a=0;
b=0;

def port(a):
    b=int(a,16);       #string to int/hex_int conversion 
    b0=b&0x01;         #Masking 1st bit
    b1=(b&0x02)>>1;    #Masking 2nd bit and shift to LSB
    b2=(b&0x04)>>2;    #Masking 3rd bit and shift to LSB
    b3=(b&0x08)>>3;    #Masking 4th bit and shift to LSB
    b4=(b&0x10)>>4;    #Masking 5th bit and shift to LSB
    b5=(b&0x20)>>5;    #Masking 6th bit and shift to LSB
    b6=(b&0x40)>>6;    #Masking 7th bit and shift to LSB
    b7=(b&0x80)>>7;    #Masking 8th bit and shift to LSB
    GPIO.output(chan_list, (b7,b6,b5,b4,b3,b2,b1,b0)); #8 bits (Bit 0 is 21(LSB), Bit 7 is 3(MSB))


sev_seg=[0xc0,0xf9,0xa4,0xb0,0x99,0x92,0x82,0xf8,0x80,0x90]; #Load Hex values from 0 to 9 (Common Anode)

while True:                               #To display 00 to 99 continuously
    for i in range(0,len(sev_seg)):
        for j in range(0,len(sev_seg)):
            GPIO.output(ctrl_pins,(0,1))   # control Pin 16 for 1st segment
            port(sev_seg[i])               #Data for 1st segment
            time.sleep(0.05);              #50 ms delay 
            
            GPIO.output(ctrl_pins,(1,0))  # control Pin 12 for 2nd segment
            port(sev_seg[j]);             #Data for 2nd segment
            time.sleep(0.02);             #20 ms delay 
                      
GPIO.cleanup() #Finally to reset all GPIO pins
