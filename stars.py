#!/usr/bin/env python
'''
CW telemetry decoder for the STARS satellite 
Author: Kay(github.com/kayhe)
Additional information on the STARS project:
    stars.eng.shizuoka.ac.jp/english.html
'''
import math

m2 = raw_input("M2(if available):")
m3 = raw_input("M3:")
m4 = raw_input("M4(if available):")
m5 = raw_input("M5:")
m6 = raw_input("M6(if available):")
factor = 5.0/255.0

def check(data):
    if(len(data) != 8):
        raise Exception("Missing values!")
        exit()

def convert(old):
    new = [0,0,0,0,0,0,0,0]
    for i in range(7):
        new[i] = int(old[i],16)
    return new

def temperature(temp):
    lnterm = (50.0 * temp / 255) / (5 - 5.0 * temp / 255)
    newtemp = -24.96 * math.log(lnterm,math.e) + 87.802
    return newtemp

def m2decode(data):
    check(data)
    data = convert(data)
    time = data[0] * 16**5 + data[1] * 16**4 + data[2] * 16**3 + data[3] * 16**2 + data[4] * 16 + data[5]
    print "Timestamp[s] = ", time
    print "Timestamp[h] = ", time/3600.0
    condition = data[6] * 16 + data[7]
    if(condition != 0):
        print "\tMission cannot be started!"
    print "\n"

def m3decode(data):
    check(data)
    data = convert(data)
    rssi = (data[0] * 16 + data[1])/2.0
    print "RSSI = ", rssi
    temp1 = data[2] * 16 + data[3]
    print "Temperature 1[degC] = ", temperature(temp1)
    temp2 = data[4] * 16 + data[5]
    print "Temperature 2[degC] = ", temperature(temp2)
    temp3 = data[6] * 16 + data[7]
    print "Temperature 3[degC] = ", temperature(temp3)
    print "\n"

def m4decode(data):
    check(data)
    convert(data)
    mode = data[0] * 16 + data[1]
    if(mode == 2):
        print "Primary mode"
    elif(mode == 130):
        print "Normal mode"
    elif(mode in [128,136,138,144,146,152,154,160,162,168,170,176,178,184,186]):
        print "Mission mode"
    elif(mode in [134,142,192,194,196,198,200,202,206,208,216]):
        print "Emergency mode"
    reset_time = data[2] * 16 + data[3]
    print "Reset time of COM system = ", reset_time
    receive_times = data[6] * 16 + data[7]
    print "Receive times of CDH system = ", receive_times
    print "\n"

def m5decode(data):
    check(data)
    data = convert(data)
    solar_current = (data[0] * 16 + data[1]) * factor * 1/2.48
    print "Solar cell current[A] = ", solar_current
    solar_voltage = (data[2] * 16 + data[3]) * factor * 10/3.33
    print "Solar cell voltage[V] = ", solar_voltage
    total_current = (data[4] * 16 + data[5]) * factor * 1/0.78
    print "Total system current[A] = ", total_current
    total_voltage = (data[6] * 16 + data[7]) * factor * 10/3.33
    print "Total system voltage[V] = ", total_voltage
    print "\n"
def m6decode(data):
    check(data)
    data = convert(data)
    solar_voltage = (data[0] * 16**3 + data[1] * 16**2 + data[2] * 16 + data[3]) * factor * 10/3.33
    print "Solar cell voltage(CDH)[V] = ", solar_voltage
    total_voltage = (data[4] * 16**3 + data[5] * 16**2 + data[6] * 16 + data[7]) * factor * 10/3.33 
    print "Total voltage(CDH)[V] = ", total_voltage
    print "\n"

if(m2 != ''):
    m2decode(m2)
m3decode(m3)
if(m4 != ''):
    m4decode(m4)
m5decode(m5)
if(m6 != ''):
    m6decode(m6)
