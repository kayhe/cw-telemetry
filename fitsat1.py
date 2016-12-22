#!/usr/bin/env python
'''
Telemetry decoder for FITSAT1 437MHz CW downlink
Author: Kay(github.com/kayhe)
More information on FITSAT1 and sample telemetry data
can be found here:
    www.fit.ac.jp/~tanaka/fitsat.shtml
'''
s1 = raw_input("S1 value:")
s2 = raw_input("S2 value:")
s3 = raw_input("S3 value:")
s4 = raw_input("S4 value:")
s5 = raw_input("S5 value:")
factor = 5.0/256.0
factor2 = 4.5/256.0

def divide(old):
    new = [old[i:i+2] for i in range(0, len(old),2)]
    if(len(new) != 4):
        raise Exception("Values missing!")
        exit()
    return new

def s1decode(data):
    data = divide(data)
    rssi, voltage, current, batt_current = data
    rssi = int(rssi, 16) * factor 
    print "RSSI 437MHz[V] = ", rssi 
    voltage = int(voltage, 16) * factor
    print "Total voltage of solar panel[V] = ", voltage 
    current = int(current, 16) * factor * 0.4
    print "Total current of solar panel[A] = ", current 
    batt_current = int(batt_current, 16) * factor
    print "Voltage of one cell lithium ion battery[V] = ", batt_current 
    print "\n"

def s2decode(data):
    data = divide(data)
    current_single, voltage_3, current_3, voltage_reference = data
    current_single = (int(current_single, 16) * factor - 2.5) * 0.4
    print "Current of single cell lithium ion battery[A] = ", current_single
    if(current_single > 0):
        print("\tDischarging")
    else:
        print("\tCharging")
    voltage_3 = int(voltage_3,16) * factor * 3
    print "Voltage of 3 cells lithium ion battery[V] = ",voltage_3
    current_3 = (int(current_3, 16) * factor - 2.5) * 10 
    print "Current of 3 cells lithium ion battery[A] = ", current_3
    if(current_3 > 0):
        print("\tDischarging")
    else:
        print("\tCharging")
    voltage_reference = int(voltage_reference, 16) * factor
    print "Voltage reference(2.5V)[V] = ", voltage_reference
    print "\n"

def s3decode(data):
    data = divide(data)
    voltage_x, voltage_y, voltagex, voltagey = data
    voltage_x = int(voltage_x, 16) * factor2 * 2
    print "Voltage of +X panel[V] = ", voltage_x
    voltage_y = int(voltage_y, 16) * factor2 * 2
    print "Voltage of +Y panel[V] = ", voltage_y
    voltagex = int(voltagex, 16) * factor2 * 2
    print "Voltage of -X panel[V] = ", voltagex
    voltagey = int(voltagey, 16) * factor2 * 2
    print "Voltage of -Y panel[V] = ", voltagey
    print "\n"

def s4decode(data):
    data = divide(data)
    temp_3, temp_single, temp_z, tempz = data
    temp_3 = (int(temp_3,16) * factor2 - 0.5)/0.01
    print "Temperature of 3 cell battery[degC] = ", temp_3
    temp_single = (int(temp_single,16) * factor2 - 0.5)/0.01
    print "Temperature of single cell battery[degC] = ", temp_single
    temp_z = (int(temp_z,16) * factor2 - 0.5)/0.01
    print "Temperature of +Z panel[degC] = ", temp_z
    tempz = (int(tempz,16) * factor2 - 0.5)/0.01
    print "Temperature of -Z panel[degC] = ", tempz
    print "\n"

def s5decode(data):
    data = divide(data)
    rssi, time1, time2, time3 = data
    rssi = int(rssi, 16) * factor2
    print "RSSI 1.2GHz[V] = ", rssi
    time = int(time1,16) * 65536 + int(time2,16) * 256 + int(time3,16)
    time = time/3600.0
    print "Timestamp[h] = ", time

s1decode(s1)
s2decode(s2)
s3decode(s3)
s4decode(s4)
s5decode(s5)
