from DroneWt import DS , up , tsks
from pwn import *

def packetHandler(s , main_edit):
    if(s[:2] == b'\xAA\xAA'):
        op = s[2]
        if(op == 1):
            length = s[3]
            roll = int.from_bytes(s[4:6], byteorder='big' , signed=True)/100.0
            pitch = int.from_bytes(s[6:8], byteorder='big' , signed=True)/100.0
            yaw = int.from_bytes(s[8:10], byteorder='big' , signed=True)/100.0
            height = int.from_bytes(s[10:14], byteorder='big' , signed=False)
            DS.updatePose(roll , pitch , yaw , height)
            main_edit.nametowidget('.!frame.!frame.!label').config(text = 'Roll : %.2f'%DS.roll)
            main_edit.nametowidget('.!frame.!frame.!label2').config(text = 'Pitch : %.2f'%DS.pitch)
            main_edit.nametowidget('.!frame.!frame.!label3').config(text = 'Yaw : %.2f'%DS.yaw)
            main_edit.nametowidget('.!frame.!frame.!label13').config(text = 'Height : %.2f'%DS.height)
            # print('length : %d , roll : %.3f , pitch : %.3f , yaw : %.3f' % (length , roll , pitch , yaw))

def checkSum(*args):

    sum = 0
    for v in args:
        sum += v & 0xff
        sum += (v & 0xff00)>>8
    checksum = sum & 0xff
    return checksum

def PID1():
    
    packet = b'\xAA\xAF'
    packet += b'\x10'
    packet += b'\x12'
    packet += p16(up.p1)
    packet += p16(up.i1)
    packet += p16(up.d1)
    packet += p16(up.p2)
    packet += p16(up.i2)
    packet += p16(up.d2)
    packet += p16(up.p3)
    packet += p16(up.i3)
    packet += p16(up.d3)
    packet += p16(up.p4)
    packet += p16(up.i4)
    packet += p16(up.d4)
    packet += p16(up.p1_rate)
    packet += p16(up.i1_rate)
    packet += p16(up.d1_rate)
    packet += p16(up.p2_rate)
    packet += p16(up.i2_rate)
    packet += p16(up.d2_rate)
    packet += p16(up.p3_rate)
    packet += p16(up.i3_rate)
    packet += p16(up.d3_rate)
    packet += p16(up.p4_rate)
    packet += p16(up.i4_rate)
    packet += p16(up.d4_rate)
    checksum = checkSum(up.p1 , up.i1 , up.d1 , up.p2 , up.i2 , up.d2 , up.p3 , up.i3 , up.d3 , up.p4 , up.i4 , up.d4 , up.p1_rate , up.i1_rate , up.d1_rate , up.p2_rate , up.i2_rate , up.d2_rate , 
    up.p3_rate , up.i3_rate , up.d3_rate , up.p4_rate , up.i4_rate , up.d4_rate)
    packet += p8(checksum)
    print(packet)
    return packet
    

def TSK1():
    packet = b'\xAA\xAF'
    packet += b'\x13'
    packet += b'\x12'
    print(tsks.tskp)
    print(tsks.tskf)
    packet += p16(tsks.tskp[0])
    packet += p16(tsks.tskf[0])
    packet += p16(tsks.tskp[1])
    packet += p16(tsks.tskf[1])
    packet += p16(tsks.tskp[2])
    packet += p16(tsks.tskf[2])
    packet += p16(tsks.tskp[3])
    packet += p16(tsks.tskf[3])
    packet += p16(tsks.tskp[4])
    packet += p16(tsks.tskf[4])
    packet += p16(tsks.tskp[5])
    packet += p16(tsks.tskf[5])
    packet += p16(tsks.tskp[6])
    packet += p16(tsks.tskf[6])
    packet += p16(tsks.tskp[7])
    packet += p16(tsks.tskf[7])
    checksum = checkSum(tsks.tskp[0] , tsks.tskf[0] , tsks.tskp[1] , tsks.tskf[1] ,tsks.tskp[2] , tsks.tskf[2] , tsks.tskp[3] , tsks.tskf[3] 
        , tsks.tskp[4] , tsks.tskf[4] , tsks.tskp[5] , tsks.tskf[5] , tsks.tskp[6] , tsks.tskf[6] , tsks.tskp[7] , tsks.tskf[7])
    packet += p8(checksum)
    print(packet)

    return 1
    
