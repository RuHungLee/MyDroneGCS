
class DroneStatus():

    def __init__(self , roll , pitch , yaw , height):
        
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw 
        self.height = height 

    def updatePose(self , roll , pitch , yaw , height):
        
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw 
        self.height = height 

class DroneUpdate():

    def __init__(self, p1 , i1 , d1 , p2 , i2 , d2 ,  p3 , i3 , d3 , p1_rate , i1_rate , d1_rate , p2_rate , i2_rate , d2_rate ,  p3_rate , i3_rate , d3_rate ,  
    
    p4 , i4 , d4 , p4_rate , i4_rate , d4_rate , thr , roll , pitch , yaw):
        
        self.p1 = int(float(p1)*1000)
        self.i1 = int(float(i1)*1000)
        self.d1 = int(float(d1)*1000)
        self.p2 = int(float(p2)*1000)
        self.i2 = int(float(i2)*1000)
        self.d2 = int(float(d2)*1000)
        self.p3 = int(float(p3)*1000)
        self.i3 = int(float(i3)*1000)
        self.d3 = int(float(d3)*1000)
        self.p4 = int(float(p4)*1000)
        self.i4 = int(float(i4)*1000)
        self.d4 = int(float(d4)*1000)
        self.p1_rate = int(float(p1_rate)*1000)
        self.i1_rate = int(float(i1_rate)*1000)
        self.d1_rate = int(float(d1_rate)*1000)
        self.p2_rate = int(float(p2_rate)*1000)
        self.i2_rate = int(float(i2_rate)*1000)
        self.d2_rate = int(float(d2_rate)*1000)
        self.p3_rate = int(float(p3_rate)*1000)
        self.i3_rate = int(float(i3_rate)*1000)
        self.d3_rate = int(float(d3_rate)*1000)
        self.p4_rate = int(float(p4_rate)*1000)
        self.i4_rate = int(float(i4_rate)*1000)
        self.d4_rate = int(float(d4_rate)*1000)
        self.thr = int(thr)
        self.roll = int(roll)
        self.pitch = int(pitch)
        self.yaw = int(yaw)

    def update(self, p1 , i1 , d1 , p2 , i2 , d2 ,  p3 , i3 , d3 , p1_rate , i1_rate , d1_rate , p2_rate , i2_rate , d2_rate ,  p3_rate , i3_rate , d3_rate ,  
    
    p4 , i4 , d4 , p4_rate , i4_rate , d4_rate , thr , roll , pitch , yaw):
        
        self.p1 = int(float(p1)*1000)
        self.i1 = int(float(i1)*1000)
        self.d1 = int(float(d1)*1000)
        self.p2 = int(float(p2)*1000)
        self.i2 = int(float(i2)*1000)
        self.d2 = int(float(d2)*1000)
        self.p3 = int(float(p3)*1000)
        self.i3 = int(float(i3)*1000)
        self.d3 = int(float(d3)*1000)
        self.p4 = int(float(p4)*1000)
        self.i4 = int(float(i4)*1000)
        self.d4 = int(float(d4)*1000)
        self.p1_rate = int(float(p1_rate)*1000)
        self.i1_rate = int(float(i1_rate)*1000)
        self.d1_rate = int(float(d1_rate)*1000)
        self.p2_rate = int(float(p2_rate)*1000)
        self.i2_rate = int(float(i2_rate)*1000)
        self.d2_rate = int(float(d2_rate)*1000)
        self.p3_rate = int(float(p3_rate)*1000)
        self.i3_rate = int(float(i3_rate)*1000)
        self.d3_rate = int(float(d3_rate)*1000)
        self.p4_rate = int(float(p4_rate)*1000)
        self.i4_rate = int(float(i4_rate)*1000)
        self.d4_rate = int(float(d4_rate)*1000)
        self.thr = int(thr)
        self.roll = int(roll)
        self.pitch = int(pitch)
        self.yaw = int(yaw)


    def transferP(self):
       
       # 傳送 mavlink 封包
       print('transfer')

DS = DroneStatus(0,0,0,0)
up = DroneUpdate(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)