from threading import Thread
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

        try:
            if(self.connect == 0):

                self.connect = 1
                self.sockSnd = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
                self.sockRcv = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
                self.sockRcv.bind(('' , self.lport))
                Thread(target = self.recv , daemon = True).start()
                self.main_edit.nametowidget('!button').config(text = '斷開連接')

            elif(self.connect == 1):

                self.connect = 0
                self.sockSnd.close()
                self.sockRcv.close()
                self.main_edit.nametowidget('!button').config(text = '開始連接')
        
        except:
            print('連接失敗...')
            sys.exit()
    
    def recv(self):
        
        while 1:
            if(self.connect == 1):
                try:
                    self.n = self.n + 1
                    self.sockRcv.settimeout(0.0001)
                    d , s = self.sockRcv.recvfrom(1024)
                    print("received message: %s" % s)
                except socket.timeout:
                    self.n = 0
                    print("時間到")


udpserv = udpServ(8086 , '192.168.4.1' , 8086)


