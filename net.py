from threading import Thread
from proto import packetHandler , PID1 , TSK1
import socket
import time
import sys


class udpServ():
    
    def __init__(self , lport , rip , rport):
        
        self.lport = lport
        self.rip = rip
        self.rport = rport
        self.connect = 0
        self.sockSnd = None
        self.sockRcv = None
        self.main_edit = None
        self.n = 0

    def update(self , lport , rip , rport , main_edit):
        
        self.lport = lport
        self.rip = rip
        self.rport = rport
        self.main_edit = main_edit
    
    def cnt(self):


            if(self.connect == 0):

                self.connect = 1
                self.main_edit.nametowidget('!button').config(text = '斷開連接')
                self.sockSnd = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
                self.sockRcv = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
                self.sockRcv.bind(('' , self.lport))
                Thread(target = self.recv , daemon = True).start()

            elif(self.connect == 1):

                self.connect = 0
                self.sockSnd.close()
                self.sockRcv.close()
                self.main_edit.nametowidget('!button').config(text = '開始連接')
        

    def recv(self):
        
        while 1:

            try:

                self.sockRcv.settimeout(1)
                s , d = self.sockRcv.recvfrom(1024)
                packetHandler(s , self.main_edit)
                # print("received message: " , s)
                
            except socket.timeout:

                print('時間到')

    def sendPID1(self):
        
        if(self.connect == 1):
            msg = PID1()
            print('send...')
            for i in range(5):
                self.sockSnd.sendto(msg, (self.rip , self.rport))
        else:
            print('尚未連接')

    def sendTSK1(self):

        if(self.connect == 1):
            msg = TSK1()
            print('send...')
            for i in range(5):
                self.sockSnd.sendto(msg, (self.rip , self.rport))
        else:
            print('尚未連接')

udpserv = udpServ(8086 , '192.168.4.1' , 8086)


