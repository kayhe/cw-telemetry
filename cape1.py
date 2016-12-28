#!/usr/bin/env python
'''
CW beacon decoder for CAPE-1 cubesat
Author: Kay(github.com/kayhe)
'''
row1 = raw_input("k5usl 1 ")
row2 = raw_input("k5usl 2 ")
row3 = raw_input("k5usl 3 ")

def convertsigned(value):
    if(value > 128):
        return value - 256
    else:
        return value

def splitdata(string):
    data = [string[i:i+2] for i in range(0,len(string),2)]
    return data

data1 = splitdata(row1)
if(len(data1) != 8 and len(data1) != 0):
    raise Exception("Insufficient dataset: row1")
data2 = splitdata(row2)
if(len(data2) != 9 and len(data2) != 0):
    raise Exception("Insufficient dataset: row2")
data3 = splitdata(row3)
if(len(data3) != 6 and len(data3) != 0):
    raise Exception("Insufficient dataset: row3")

#k5usl 1
if(len(data1) != 0):
    print "MPB Voltage: ", int(data1[0],16) * 0.02, " V"
    print "HPB Voltage: ", int(data1[1],16) * 0.02, " V"
    print "Battery 1 Voltage: ", int(data1[2],16) * 0.02, " V"
    print "Battery 2 Voltage: ", int(data1[3],16) * 0.02, " V"
    print "Battery 1 Current generated: ", int(data1[4],16), " mA"
    print "Battery 1 Current absorbed: ", int(data1[5],16), " mA"
    print "Battery 2 Current generated: ", int(data1[6],16), " mA"
    print "Battery 2 Current absorbed: ", int(data1[7],16), " mA"
#k5usl 2
if(len(data2) != 0):
    print "Battery 1 Temperature: ", convertsigned(int(data2[0],16)), " degC"
    print "X+ Temperature: ", convertsigned(int(data2[1],16)), " degC"
    print "X- Temperature: ", convertsigned(int(data2[2],16)), " degC"
    print "Y+ Temperature: ", convertsigned(int(data2[3],16)), " degC"
    print "Y- Temperature: ", convertsigned(int(data2[4],16)), " degC"
    print "Z+ Temperature: ", convertsigned(int(data2[5],16)), " degC"
    print "Z- Temperature: ", convertsigned(int(data2[6],16)), " degC"
    print "RFamp Temperature: ", convertsigned(int(data2[7],16)), " degC"
    print "Battery 2 Temperature: ", convertsigned(int(data2[8],16)), " degC"
#k5usl 3
if(len(data3) != 0):
    print "Solar Panel Current X+: ", int(data3[0],16), " mA"
    print "Solar Panel Current X-: ", int(data3[1],16), " mA"
    print "Solar Panel Current Y+: ", int(data3[2],16), " mA"
    print "Solar Panel Current Y-: ", int(data3[3],16), " mA"
    print "Solar Panel Current Z+: ", int(data3[4],16), " mA"
    print "Solar Panel Current Z-: ", int(data3[5],16), " mA" 
