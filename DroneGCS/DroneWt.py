

class DroneStatus():

    def __init__(self , roll , pitch , yaw):
        
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw 

    def updatePose(self , roll , pitch , yaw):
        
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw 



class DroneUpdate():

    def __init__(self, p1 , i1 , d1 , p2 , i2 , d2 ,  p3 , i3 , d3 , thr , roll , pitch , yaw):
        
        self.p1 = int(float(p1)*100)
        self.i1 = int(float(i1)*100)
        self.d1 = int(float(d1)*100)
        self.p2 = int(float(p2)*100)
        self.i2 = int(float(i2)*100)
        self.d2 = int(float(d2)*100)
        self.p3 = int(float(p3)*100)
        self.i3 = int(float(i3)*100)
        self.d3 = int(float(d3)*100)
        self.thr = int(thr)
        self.roll = int(roll)
        self.pitch = int(pitch)
        self.yaw = int(yaw)

    def update(self, p1 , i1 , d1 , p2 , i2 , d2 ,  p3 , i3 , d3 , thr , roll , pitch , yaw):
        
        self.p1 = int(float(p1)*100)
        self.i1 = int(float(i1)*100)
        self.d1 = int(float(d1)*100)
        self.p2 = int(float(p2)*100)
        self.i2 = int(float(i2)*100)
        self.d2 = int(float(d2)*100)
        self.p3 = int(float(p3)*100)
        self.i3 = int(float(i3)*100)
        self.d3 = int(float(d3)*100)
        self.thr = int(thr)
        self.roll = int(roll)
        self.pitch = int(pitch)
        self.yaw = int(yaw)


    def transferP(self):
       
       # 傳送 mavlink 封包
       print('transfer')

DS = DroneStatus(0,0,0)
up = DroneUpdate(0,0,0,0,0,0,0,0,0,0,0,0,0)