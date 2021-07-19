from cntPage import *
from tkinter import *
from DroneWt import *
from proto import *
from plot import *
from functools import partial
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import animation, figure


postPage = list()
postPageFirst = 0
dv1 = None

def animate(self, *args):
    print('ani')
    xs.append(time.clock())
    ys.append(time.clock() + np.random.random())
    xs = xs[-100:]
    ys = ys[-100:]
    ax1.clear()
    ax1.plot(xs, ys)

# 飛控姿態控制頁面配置
def open_post(main_edit):

    global postPage , postPageFirst , dv1

    clean_main(main_edit)

    if(postPageFirst == 1):

        resume_postPage()

    else:
        
        # PID title 
        pidt = tk.Label(main_edit , font=("Arial Bold", 15) , text = 'PID 參數設定' , anchor="w" , justify=LEFT )
        
        # roll PID
        p1n = tk.Label(main_edit , text = 'roll P : ' , anchor="w" , justify=RIGHT , width = 8)
        p1 = tk.Entry(main_edit)
        p1.insert(END , '0')
        i1n = tk.Label(main_edit , text = 'roll I : ' , anchor="w" , justify=LEFT , width = 8)
        i1 = tk.Entry(main_edit)
        i1.insert(END , '0')
        d1n = tk.Label(main_edit , text = 'roll D : ' , anchor="w" , justify=LEFT , width = 8)
        d1 = tk.Entry(main_edit)
        d1.insert(END , '0')
        pidt.grid(row=0, column=0,  padx = (75 , 20) , pady= 30)
        p1n.grid(row=1, column=0,  padx = 20, pady= 10)
        p1.grid(row=1, column=1, padx = 20 , pady= 10)
        i1n.grid(row=2, column=0, padx = 20 , pady= 10)
        i1.grid(row=2, column=1, padx = 20 , pady= 10)
        d1n.grid(row=3 , column=0 , padx = 20 , pady= 10)
        d1.grid(row=3 , column=1 , padx = 20 , pady= 10)

        # pitch PID
        p2n = tk.Label(main_edit , text = 'pitch P : ' , anchor="w" , justify=LEFT , width = 8)
        p2 = tk.Entry(main_edit)
        p2.insert(END , '0')
        i2n = tk.Label(main_edit , text = 'pitch I : ' , anchor="w" , justify=LEFT , width = 8)
        i2 = tk.Entry(main_edit)
        i2.insert(END , '0')
        d2n = tk.Label(main_edit , text = 'pitch D : ', anchor="w" , justify=LEFT , width = 8)
        d2 = tk.Entry(main_edit)
        d2.insert(END , '0')
        p2n.grid(row=4, column=0,  padx = 20, pady= 10)
        p2.grid(row=4, column=1, padx = 20 , pady= 10)
        i2n.grid(row=5, column=0, padx = 20 , pady= 10)
        i2.grid(row=5, column=1, padx = 20 , pady= 10)
        d2n.grid(row=6 , column=0 , padx = 20 , pady= 10)
        d2.grid(row=6 , column=1 , padx = 20 , pady= 10)

        # yaw PID
        p3n = tk.Label(main_edit , text = 'yaw P : ' , anchor="w" , justify=LEFT , width = 8)
        p3 = tk.Entry(main_edit)
        p3.insert(END , '0')
        i3n = tk.Label(main_edit , text = 'yaw I : ' , anchor="w" , justify=LEFT , width = 8)
        i3 = tk.Entry(main_edit)
        i3.insert(END , '0')
        d3n = tk.Label(main_edit , text = 'yaw D : ' , anchor="w" , justify=LEFT , width = 8)
        d3 = tk.Entry(main_edit)
        d3.insert(END , '0')
        p3n.grid(row=7, column=0,  padx = 20, pady= 10)
        p3.grid(row=7, column=1, padx = 20 , pady= 10)
        i3n.grid(row=8, column=0, padx = 20 , pady= 10)
        i3.grid(row=8, column=1, padx = 20 , pady= 10)
        d3n.grid(row=9 , column=0 , padx = 20 , pady= 10)
        d3.grid(row=9 , column=1 , padx = 20 , pady= 10)

        # roll rate PID
        p1n_rate = tk.Label(main_edit , text = 'roll rate P : ' , anchor="w" , justify=LEFT , width = 25)
        p1_rate = tk.Entry(main_edit)
        p1_rate.insert(END , '0')
        i1n_rate = tk.Label(main_edit , text = 'roll rate I : ' , anchor="w" , justify=LEFT , width = 25)
        i1_rate = tk.Entry(main_edit)
        i1_rate.insert(END , '0')
        d1n_rate = tk.Label(main_edit , text = 'roll rate D : ' , anchor="w" , justify=LEFT , width = 25)
        d1_rate = tk.Entry(main_edit)
        d1_rate.insert(END , '0')
        p1n_rate.grid(row=1, column=2,  padx = 20, pady= 10)
        p1_rate.grid(row=1, column=3, padx = 20 , pady= 10)
        i1n_rate.grid(row=2, column=2, padx = 20 , pady= 10)
        i1_rate.grid(row=2, column=3, padx = 20 , pady= 10)
        d1n_rate.grid(row=3 , column=2 , padx = 20 , pady= 10)
        d1_rate.grid(row=3 , column=3 , padx = 20 , pady= 10)

        # pitch rate PID
        p2n_rate = tk.Label(main_edit , text = 'pitch rate P : ' , anchor="w" , justify=LEFT , width = 25)
        p2_rate = tk.Entry(main_edit)
        p2_rate.insert(END , '0')
        i2n_rate = tk.Label(main_edit , text = 'pitch rate I : ' , anchor="w" , justify=LEFT , width = 25)
        i2_rate = tk.Entry(main_edit)
        i2_rate.insert(END , '0')
        d2n_rate = tk.Label(main_edit , text = 'pitch rate D : ', anchor="w" , justify=LEFT , width = 25)
        d2_rate = tk.Entry(main_edit)
        d2_rate.insert(END , '0')
        p2n_rate.grid(row=4, column=2,  padx = 20, pady= 10)
        p2_rate.grid(row=4, column=3, padx = 20 , pady= 10)
        i2n_rate.grid(row=5, column=2, padx = 20 , pady= 10)
        i2_rate.grid(row=5, column=3, padx = 20 , pady= 10)
        d2n_rate.grid(row=6 , column=2 , padx = 20 , pady= 10)
        d2_rate.grid(row=6 , column=3 , padx = 20 , pady= 10)

        # yaw rate PID
        p3n_rate = tk.Label(main_edit , text = 'yaw rate P : ' , anchor="w" , justify=LEFT , width = 25)
        p3_rate = tk.Entry(main_edit)
        p3_rate.insert(END , '0')
        i3n_rate = tk.Label(main_edit , text = 'yaw rate I : ' , anchor="w" , justify=LEFT , width = 25)
        i3_rate = tk.Entry(main_edit)
        i3_rate.insert(END , '0')
        d3n_rate = tk.Label(main_edit , text = 'yaw rate D : ' , anchor="w" , justify=LEFT , width = 25)
        d3_rate = tk.Entry(main_edit)
        d3_rate.insert(END , '0')
        p3n_rate.grid(row=7, column=2 ,  padx = 20, pady= 10)
        p3_rate.grid(row=7, column=3 , padx = 20 , pady= 10)
        i3n_rate.grid(row=8, column=2 , padx = 20 , pady= 10)
        i3_rate.grid(row=8, column=3 , padx = 20 , pady= 10)
        d3n_rate.grid(row=9 , column=2 , padx = 20 , pady= 10)
        d3_rate.grid(row=9 , column=3 , padx = 20 , pady= 10)


        # throttle and angle title
        pos =  tk.Label(main_edit , font=("Arial Bold", 15) , text = 'PWN 值 / 姿態角' , anchor="w" , justify=LEFT)
        
        # throttle and angle value
        thrn = tk.Label(main_edit , text = 'throttle : ' , anchor="w" , justify=LEFT , width = 8)
        thr = tk.Entry(main_edit)
        thr.insert(END , '0')
        rolln = tk.Label(main_edit , text = 'roll : ' , anchor="w" , justify=LEFT , width = 8)
        roll = tk.Entry(main_edit)
        roll.insert(END , '0')
        pitchn = tk.Label(main_edit , text = 'pitch : ' , anchor="w" , justify=LEFT , width = 8)
        pitch = tk.Entry(main_edit)
        pitch.insert(END , '0')
        yawn = tk.Label(main_edit , text = 'yaw : ' , anchor="w" , justify=LEFT , width = 8)
        yaw = tk.Entry(main_edit)
        yaw.insert(END , '0')
        pos.grid(row = 10 , column=0,  padx = (110 , 20) , pady= 30)
        thrn.grid(row=11, column=0,  padx = 20, pady= (30 , 10))
        thr.grid(row=11, column=1, padx = 20 , pady= (30 , 10))
        rolln.grid(row=12, column=0, padx = 20 , pady= 10)
        roll.grid(row=12, column=1, padx = 20 , pady= 10)
        pitchn.grid(row=13 , column=0 , padx = 20 , pady= 10)
        pitch.grid(row=13 , column=1 , padx = 20 , pady= 10)
        yawn.grid(row=14 , column=0 , padx = 20 , pady= 10)
        yaw.grid(row=14 , column=1 , padx = 20 , pady= 10)

        # 寫入飛控
        btn_setPID = tk.Button(main_edit , text="寫入飛控", command=partial(writeinPID , main_edit)) # 按下後顯示實時測試頁面
        btn_setPID.grid(row=15 , column=0, sticky="ew", padx = (110 , 10) , pady= (50 , 10))

        postFrame = tk.Frame(main_edit , padx=30)
        postFrame.grid(row=13 , column=5 , columnspan=8 , rowspan=9 , padx = 10 , pady = 30)
        postRoll = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'Roll : 0.00' , anchor="w" , justify=LEFT , width = 15)
        postPitch = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'Pitch : 0.00' , anchor="w" , justify=LEFT , width = 15)
        postYaw = tk.Label(postFrame , font=("Arial Bold", 15), text = 'Yaw : 0.00' , anchor="w" , justify=LEFT , width = 15)
        accX = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'ACC_X : 0.00' , anchor="w" , justify=LEFT , width = 15)
        accY = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'ACC_Y : 0.00' , anchor="w" , justify=LEFT , width = 15)
        accZ = tk.Label(postFrame , font=("Arial Bold", 15), text = 'ACC_Z : 0.00' , anchor="w" , justify=LEFT , width = 15)
        gyroX = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'GYRO_X : 0.00' , anchor="w" , justify=LEFT , width = 15)
        gyroY = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'GYRO_Y : 0.00' , anchor="w" , justify=LEFT , width = 15)
        gyroZ = tk.Label(postFrame , font=("Arial Bold", 15), text = 'GYRO_Z : 0.00' , anchor="w" , justify=LEFT , width = 15)
        magX = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'MAG_X : 0.00' , anchor="w" , justify=LEFT , width = 15)
        magY = tk.Label(postFrame , font=("Arial Bold", 15) , text = 'MAG_Y : 0.00' , anchor="w" , justify=LEFT , width = 15)
        magZ = tk.Label(postFrame , font=("Arial Bold", 15), text = 'MAG_Z : 0.00' , anchor="w" , justify=LEFT , width = 15)

        postRoll.grid(row=0 , column=0 ,  padx = (0 , 30) , pady= 10) 
        postPitch.grid(row=1 , column=0 ,  padx = (0 , 30) , pady= 10)
        postYaw.grid(row=2 , column=0 ,  padx =  (0 , 30) , pady= 10)
        accX.grid(row=0 , column=1 ,  padx =  (20 , 30), pady= 10)
        accY.grid(row=1 , column=1 ,  padx =  (20 , 30) , pady= 10)
        accZ.grid(row=2 , column=1 ,  padx =  (20 , 30), pady= 10)
        gyroX.grid(row=0 , column=2 ,  padx =  (20 , 30) , pady= 10)
        gyroY.grid(row=1 , column=2 ,  padx =  (20 , 30), pady= 10)
        gyroZ.grid(row=2 , column=2 ,  padx =  (20 , 30) , pady= 10)
        magX.grid(row=0 , column=3 ,  padx =  (20 , 30) , pady= 10)
        magY.grid(row=1 , column=3 ,  padx =  (20 , 30), pady= 10)
        magZ.grid(row=2 , column=3 ,  padx = (20 , 30) , pady= 10)

        # plotFrame = tk.Frame(main_edit)
        # plotFrame.grid(row=0 , column=4 , columnspan=10 , rowspan=10 , ipadx = 250)
        # rollViz = tk.Label(plotFrame , font=("Arial Bold", 15) , text = 'ROLL 視圖' , anchor="w" , justify=LEFT , width = 15)
        # rollViz.grid(row=0 , column=0 ,  padx = (100 , 30) , pady= 10) 
        # # fig = figure.Figure(figsize=(15, 6), dpi=80)
        # dv1 = DV.update(15 , 6 , 80 , plotFrame)

        #delte plot frame.
        for item in [pidt , p1n , p1 ,i1n , i1 , d1n , d1 , p2n , p2 , i2n , i2 , d2n , d2 , p3n , p3 , i3n , i3 , d3n , d3 
         , p1n_rate , p1_rate ,i1n_rate , i1_rate , d1n_rate , d1_rate , p2n_rate , p2_rate , i2n_rate , i2_rate , d2n_rate , d2_rate , p3n_rate , p3_rate , i3n_rate , i3_rate , d3n_rate , d3_rate 
         , pos , thrn , thr , rolln , roll , pitchn , pitch , yawn , yaw , btn_setPID , postFrame]:
            postPage.append(item)

        postPageFirst = 1

def writeinPID(main_edit):

    # wlist =  main_edit.winfo_children()
    entryAry = list()
    for w in postPage:
        if(isinstance(w , tk.Entry)):
            entryAry.append(w)
    up.update(entryAry[0].get() , entryAry[1].get() , entryAry[2].get() , entryAry[3].get() ,
    entryAry[4].get() , entryAry[5].get() , entryAry[6].get() , entryAry[7].get() , entryAry[8].get() , 
    entryAry[9].get() , entryAry[10].get() , entryAry[11].get() , entryAry[12].get() , 
    entryAry[13].get() , entryAry[14].get() , entryAry[15].get() , entryAry[16].get() ,
    entryAry[17].get() , entryAry[18].get() , entryAry[19].get() , entryAry[20].get() , entryAry[21].get())
    udpserv.sendPID1()

def resume_postPage():
    for widget in postPage:
        widget.grid()

