class DroneUpdate():

    def __init__(self, p1 , i1 , d1 , p2 , i2 , d2 ,  p3 , i3 , d3 , thr , roll , pitch , yaw):
        
        self.p1 = p1
        self.i1 = i1
        self.d1 = d1
        self.p2 = p2
        self.i2 = i2
        self.d2 = d2
        self.p3 = p3
        self.i3 = i3
        self.d3 = d3
        self.thr = thr
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def update(self, p1 , i1 , d1 , p2 , i2 , d2 ,  p3 , i3 , d3 , thr , roll , pitch , yaw):
        
        self.p1 = p1
        self.i1 = i1
        self.d1 = d1
        self.p2 = p2
        self.i2 = i2
        self.d2 = d2
        self.p3 = p3
        self.i3 = i3
        self.d3 = d3
        self.thr = thr
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def transferP():
       
       # 傳送 mavlink 封包
       print('transfer')