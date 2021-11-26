from cntPage import *
from tkinter import *
from DroneWt import *
import tkinter as tk


rtosPage = list()
rtosPageFirst = 0

def open_rtos(main_edit):


    global rtosPage , rtosPageFirst 

    clean_main(main_edit)

    if(rtosPageFirst == 1):

        resume_rtosPage()

    else:

        # PID title 
        tsks = tk.Label(main_edit , font=("Arial Bold", 15) , text = '任務排程' , anchor="w" , justify=LEFT )
        
        # tsk1
        tsk1n = tk.Label(main_edit , text = '任務一(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        print(tsk1n)
        tsk1p = tk.Entry(main_edit)
        tsk1f = tk.Entry(main_edit)
        tsk1p.insert(END , '0')
        tsk1f.insert(END , '0')
        tsks.grid(row=0, column=0,  padx = (75 , 20) , pady= 30)
        tsk1n.grid(row=1, column=0,  padx = (110 , 20) , pady= 10)
        tsk1p.grid(row=1, column=1,  padx = (110 , 20), pady= 10)
        tsk1f.grid(row=1, column=2, padx = (110 , 20) , pady= 10)
        
        # tsk2
        tsk2n = tk.Label(main_edit , text = '任務二(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        print(tsk2n)
        tsk2p = tk.Entry(main_edit)
        tsk2f = tk.Entry(main_edit)
        tsk2p.insert(END , '0')
        tsk2f.insert(END , '0')
        tsk2n.grid(row=2, column=0,  padx = (110 , 20) , pady= 10)
        tsk2p.grid(row=2, column=1,  padx = (110 , 20), pady= 10)
        tsk2f.grid(row=2, column=2, padx = (110 , 20) , pady= 10)

        # tsk3
        tsk3n = tk.Label(main_edit , text = '任務三(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        tsk3p = tk.Entry(main_edit)
        tsk3f = tk.Entry(main_edit)
        tsk3p.insert(END , '0')
        tsk3f.insert(END , '0')
        tsk3n.grid(row=3, column=0,  padx = (110 , 20) , pady= 10)
        tsk3p.grid(row=3, column=1,  padx = (110 , 20), pady= 10)
        tsk3f.grid(row=3, column=2, padx = (110 , 20) , pady= 10)


        # tsk4
        tsk4n = tk.Label(main_edit , text = '任務四(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        tsk4p = tk.Entry(main_edit)
        tsk4f = tk.Entry(main_edit)
        tsk4p.insert(END , '0')
        tsk4f.insert(END , '0')
        tsk4n.grid(row=4, column=0,  padx = (110 , 20) , pady= 10)
        tsk4p.grid(row=4, column=1,  padx = (110 , 20), pady= 10)
        tsk4f.grid(row=4, column=2, padx = (110 , 20) , pady= 10)

        # tsk5
        tsk5n = tk.Label(main_edit , text = '任務五(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        tsk5p = tk.Entry(main_edit)
        tsk5f = tk.Entry(main_edit)
        tsk5p.insert(END , '0')
        tsk5f.insert(END , '0')
        tsk5n.grid(row=5, column=0,  padx = (110 , 20) , pady= 10)
        tsk5p.grid(row=5, column=1,  padx = (110 , 20), pady= 10)
        tsk5f.grid(row=5, column=2, padx = (110 , 20) , pady= 10)

        # tsk5
        tsk6n = tk.Label(main_edit , text = '任務六(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        tsk6p = tk.Entry(main_edit)
        tsk6f = tk.Entry(main_edit)
        tsk6p.insert(END , '0')
        tsk6f.insert(END , '0')
        tsk6n.grid(row=6, column=0,  padx = (110 , 20) , pady= 10)
        tsk6p.grid(row=6, column=1,  padx = (110 , 20), pady= 10)
        tsk6f.grid(row=6, column=2, padx = (110 , 20) , pady= 10)

        # tsk5
        tsk7n = tk.Label(main_edit , text = '任務七(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        tsk7p = tk.Entry(main_edit)
        tsk7f = tk.Entry(main_edit)
        tsk7p.insert(END , '0')
        tsk7f.insert(END , '0')
        tsk7n.grid(row=7, column=0,  padx = (110 , 20) , pady= 10)
        tsk7p.grid(row=7, column=1,  padx = (110 , 20), pady= 10)
        tsk7f.grid(row=7, column=2, padx = (110 , 20) , pady= 10)

        # tsk5
        tsk8n = tk.Label(main_edit , text = '任務八(優先級/頻率) : ' , anchor="w" , justify=RIGHT , width = 15)
        tsk8p = tk.Entry(main_edit)
        tsk8f = tk.Entry(main_edit)
        tsk8p.insert(END , '0')
        tsk8f.insert(END , '0')
        tsk8n.grid(row=8, column=0,  padx = (110 , 20) , pady= 10)
        tsk8p.grid(row=8, column=1,  padx = (110 , 20), pady= 10)
        tsk8f.grid(row=8, column=2, padx = (110 , 20) , pady= 10)

        tsks_Btn = tk.Button(main_edit , text="寫入飛控", command=partial(writeinTSK , main_edit)) # 按下後顯示實時測試頁面
        tsks_Btn.grid(row=9 , column=0, sticky="ew", padx = (110 , 20) , pady= (50 , 10))

        rtosFrame = tk.Frame(main_edit)
        rtosFrame.grid(row=25 , column=0, sticky="ew" , rowspan=9 , columnspan=8 , padx = 110 , pady = 50)
        tsk1o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務一執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)
        tsk2o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務二執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)
        tsk3o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務三執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)
        tsk4o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務四執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)
        tsk5o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務五執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)
        tsk6o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務六執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)
        tsk7o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務七執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)
        tsk8o = tk.Label(rtosFrame , font=("Arial Bold", 15) , pady =  10 , text = '任務八執行頻率 (HZ) : 0         ' , anchor="w" , justify=LEFT  , width = 30)

        print(tsk1o)

        tsk1o.grid(row=1 , column=0 ) 
        tsk2o.grid(row=2 , column=0 )
        tsk3o.grid(row=3 , column=0 )
        tsk4o.grid(row=4 , column=0 )
        tsk5o.grid(row=5 , column=0 )
        tsk6o.grid(row=6 , column=0 )
        tsk7o.grid(row=7 , column=0 )
        tsk8o.grid(row=8 , column=0 )

        #delte plot frame.
        for item in [tsks , tsk1n , tsk1p , tsk1f , tsk2n , tsk2p , tsk2f , tsk3n , tsk3p , tsk3f,
        tsk4n , tsk4p , tsk4f , tsk5n , tsk5p , tsk5f , tsk6n , tsk6p , tsk6f , tsk7n , tsk7p , tsk7f , 
        tsk8n , tsk8p , tsk8f , tsks_Btn , rtosFrame]:
            rtosPage.append(item)

        rtosPageFirst = 1


def resume_rtosPage():

    for widget in rtosPage:
        print(widget)
        widget.grid()


def writeinTSK(main_edit):

    plist = list() 
    flist = list()

    ct = 0
    for w in rtosPage:
        if(isinstance(w , tk.Entry)):
            if(ct % 2 == 0):
                plist.append(int(w.get()))
            else:
                flist.append(int(w.get()))
            ct = ct + 1

    tsks.update(plist , flist)
    udpserv.sendTSK1()
