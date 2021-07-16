from DroneWt import DS , up
from pwn import *

# 仿匿名地面工作站 3.43 版協議
def packetHandler(s , main_edit):
    if(s[:2] == b'\xAA\xAA'):
        op = s[2]
        if(op == 1):
            length = s[3]
            roll = int.from_bytes(s[4:6], byteorder='big' , signed=True)/100.0
            pitch = int.from_bytes(s[6:8], byteorder='big' , signed=True)/100.0
            yaw = int.from_bytes(s[8:10], byteorder='big' , signed=True)/100.0
            DS.updatePose(roll , pitch , yaw)
            main_edit.nametowidget('.!frame.!frame.!label').config(text = 'Roll : %.2f'%DS.roll)
            main_edit.nametowidget('.!frame.!frame.!label2').config(text = 'Pitch : %.2f'%DS.pitch)
            main_edit.nametowidget('.!frame.!frame.!label3').config(text = 'Yaw : %.2f'%DS.yaw)
            # print('length : %d , roll : %.3f , pitch : %.3f , yaw : %.3f' % (length , roll , pitch , yaw))

def checkSum(*args):

    sum = 0
    for v in args:
        sum += v
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
    checksum = checkSum(up.p1 , up.i1 , up.d1 , up.p2 , up.i2 , up.d2 , up.p3 , up.i3 , up.d3)
    packet += p8(checksum)
    print(packet)
    return packet
    

    