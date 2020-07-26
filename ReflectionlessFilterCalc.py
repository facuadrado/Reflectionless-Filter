# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:04:40 2020

Low-Pass, High-Pass, Bandpass and Bandstop reflectionless filter calculator.

Reflection-Less Filter Topology created and patented by Matthew Morgan.

This script calculates the values of capacitors and inductors to develop a relfectionless filter given the desired attenuation,
frequency and characteristic impedance z0. Please refer to Matthew Morgan's book/papers for the derivation of these novel filters.

@author: facuadrado
"""
import math
import re
from si_prefix import si_format
from DisplayCircuit import *

def HighandLowPass(gk, z0, w0):
    y0 = 1/z0
    l = (gk*z0)/(2*math.pi*f0)
    c = (gk*y0)/(2*math.pi*f0)
    return l, c

def BandStopandPass(gk, z0, fl, fh):
    y0 = 1/z0
    wl = 2*math.pi*fl
    wh = 2*math.pi*fh
    w0 = math.sqrt(wl*wh)
    delta = (wh-wl)/w0
    ls = (gk*z0)/(w0*delta)
    lx = (z0*delta)/(w0*gk)
    cs = (y0*delta)/(w0*gk)
    cx = (gk*y0)/(w0*delta)
    return ls, lx, cs, cx

def calculateFrequency(frequencyType):
    flag = True
    
    while flag == True:
        try:
            strFrequency = input('Enter ' + frequencyType +' frequency: ')
            try:
                frequency = int(strFrequency)
                flag = False
            except:
                strFrequency = re.split('(\d+)',strFrequency)
                try:
                    if strFrequency[-1].lower() == 'khz':
                        frequency = int(strFrequency[1])*1000
                        flag = False
                    elif strFrequency[-1].lower() == 'mhz':
                        frequency = int(strFrequency[1])*1000000
                        flag = False
                    elif strFrequency[-1].lower() == 'ghz':
                        frequency = int(strFrequency[1])*1000000000
                        flag = False
                    else:
                        print('Acceptable format examples: 1000 or 1Khz, 1Mhz, 1Ghz.')
                except:
                    print('Acceptable format examples: 1000 or 1Khz, 1Mhz, 1Ghz.')
        except:
            print('Please enter a valid option.')
            
    return frequency
    
flag = True

while flag == True:
    userinput = input("Enter Filter Type: (Low-Pass, High-Pass, Band-Pass or Band-Stop): ")
    if userinput == "Low-Pass":
        filterType = 'lowpass'
        flag = False
    elif userinput == "High-Pass":
        filterType = 'highpass'
        flag = False
    elif userinput == "Band-Pass":
        filterType = 'bandpass'
        flag = False
    elif userinput == "Band-Stop":
        filterType = 'bandstop'
        flag = False
    elif userinput == 'exit':
        flag = False
        print('Terminating Program...')
        quit()
    else:
        print('Please enter one of the following options: ')
        print('Low-Pass')
        print('High-Pass')
        print('Band-Pass')
        print('Band-Stop')
        print('Or enter: exit to quit the program.')

flag = True

while flag == True:
    userinput = input("Enter Pass-Band Corner Frequecy Loss dB Specification or Poles(1db, 3dB or Pole Frequency): ")
    if userinput.lower() == "1db":
        gk = 0.5592
        flag = False
    elif userinput.lower() == "3db":
        gk = 0.6573
        flag = False
    elif userinput.lower() == "pole frequency":
        gk = 1
        flag = False
    elif userinput == 'exit':
        flag = False
        print('Terminating Program...')
        quit()
    else:
        print('Please enter one of the following options: ')
        print('1dB')
        print('3dB')
        print('Pole Frequency')
        print('Or enter: exit to quit the program.')

if filterType == 'bandpass' or filterType == 'bandstop':
    fl = calculateFrequency('low')   
    fh = calculateFrequency('high')  
            
else:
    f0 = calculateFrequency('cut-off')
            
flag = True

while flag == True:
    try:
        z0 = int(input("Enter impedance z0: "))
        flag = False
    except:
        print('Please enter a valid integer number.')
        
if filterType == 'lowpass' or filterType == 'highpass':
    l, c = HighandLowPass(gk, z0, f0)
    DrawCircuit(filterType, z0=str(z0)+'\u03A9', l=si_format(l, precision=2)+'H', c=si_format(c, precision=2)+'F')
else:
    ls, lx, cs, cx = BandStopandPass(gk, z0, fl, fh)
    DrawCircuit(filterType, z0=str(z0)+'\u03A9', l='N/A', c='N/A', ls=si_format(ls, precision=2)+'H', lx=si_format(lx, precision=2)+'H', cs=si_format(cs, precision=2)+'F', cx=si_format(cx, precision=2)+'F')
