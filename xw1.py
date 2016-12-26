#!/usr/bin/env python
'''
XW-1/HO-68 cw beacon decoder
Author: Kay(github.com/kayhe)
'''
notation = {'t':'0', 'a':'1', 'u':'2', 'v': '3', '4' : '4', 'e':'5',
            '6':'6', 'b':'7', 'd':'8', 'n':'9'}
print "Please enter telemetry, every group separated by a space, no capitalized letters"
inp = raw_input("Telemetry:")
data = inp.split(" ")
if(len(data) != 13):
    raise Exception("Missing data")

def convert(string):
    ret = ''
    for char in string:
        ret += notation[char]
    return int(ret)

#CH1
if(data[0] == 'aaa'):
    print "PA RF switch status: PA2 works"
elif(data[0] == 'ttt'):
    print "PA RF switch status: PA1 works"
#CH2
if(data[1] == 'ttt'):
    print "Transponder working status: Beacon only"
elif(data[1] == 'tta'):
    print "Transponder working status: Beacon and linear transponder"
elif(data[1] == 'tat'):
    print "Transponder working status: Beacon and FM transponder"
elif(data[1] == 'att'):
    print "Transponder working status: Upload software"
#CH3
temperature = data[2][1:]
temperature = convert(temperature)
if(data[2][0] == 't'):
    print 'Transponder temperature: -', temperature, ' degC'
else:
    print 'Transponder temperature: ', temperature, ' degC'
#CH4
print "Beacon RF output power: ", convert(data[3]), ' mW'
#CH5
beacon_voltage = convert(data[4]) / 100.0
print "Beacon power supply voltage: ", beacon_voltage, ' V'
#CH6
print "Beacon power supply current: ", convert(data[5]), ' mA'
#CH7
agc_voltage = convert(data[6]) / 100.0
print "Linear transponder AGC voltage: ", agc_voltage, ' V'
#CH8
transponder_out = convert(data[7]) * 3
print "Transponder RF output power: ", transponder_out, ' mW'
#CH9
print "Transponder PA power supply current: ", convert(data[8]), ' mA'
#CH10
print "Linear Transponder up converter power supply current: ", convert(data[9]), ' mA'
#CH11
linear_volt = convert(data[10]) / 100.0
print "Linear transponder power supply voltage: ", linear_volt, ' V'
#CH12
print "Store-forward transponder power supply current: ", convert(data[11]), ' mA'
#CH13
store_forward_voltage = convert(data[12]) / 100.0
print "Store-forward transponder power supply voltage: ", store_forward_voltage, ' V'
