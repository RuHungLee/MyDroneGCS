from tkinter import *
import tkinter as tk
from net import *
from functools import partial

CntPage = list()
CntPageFirst = 0

# 飛控連結頁面配置
def open_cnt(main_edit):

    global CntPage , CntPageFirst

    clean_main(main_edit)

    if(CntPageFirst == 1):
        resume_CntPage()
    else:
        # 連接表單
        CntPageFirst = 1
        cntn = tk.Label(main_edit , font=("Arial Bold", 15) , text = '飛控連接')
        ripn = tk.Label(main_edit , text = 'remote IP : ' , anchor="w" , justify=LEFT , width = 15)
        rip = tk.Entry(main_edit)
        rip.insert(END , '192.168.4.1')
        rportn = tk.Label(main_edit , text = 'remote Port : ' , anchor="w" , justify=LEFT , width = 15)
        rport = tk.Entry(main_edit)
        rport.insert(END , '8086')
        lportn = tk.Label(main_edit , text = 'local Port : ' , anchor="w" , justify=LEFT , width = 15)
        lport = tk.Entry(main_edit)
        lport.insert(END , '8086')
        
        cntn.grid(row=0, column=0,  padx = (95 , 20) , pady= 30)
        ripn.grid(row=1, column=0,  padx = (110 , 10) , pady= 10)
        rip.grid(row=1, column=1,  padx = (110 , 10) , pady= 10)
        rportn.grid(row=2, column=0, padx = (110 , 10) , pady= 10)
        rport.grid(row=2, column=1, padx = (110 , 10) , pady= 10)
        lportn.grid(row=3, column=0, padx = (110 , 10) , pady= 10)
        lport.grid(row=3 , column=1 , padx = (110 , 10) , pady= 10)

        # 開始連接
        btn_connect = tk.Button(main_edit , command = partial(udpConnect , main_edit)) # 按下後顯示實時測試頁面
        if(udpserv.connect == 0):
            btn_connect.config(text='開始連接')
        elif(udpserv.connect == 1):
            btn_connect.config(text='斷開連接')
    
        btn_connect.grid(row=4 , column=0, sticky="ew", padx = (110 , 20) , pady= 50)
        
        for item in [cntn , ripn , rip , rportn , rport , lportn , lport , btn_connect]:
            CntPage.append(item)

def udpConnect(main_edit):

    if(udpserv.connect == 0):

        entryAry = list()

        for w in CntPage:
            if(isinstance(w , tk.Entry)):
                entryAry.append(w)
        
        rip = entryAry[0].get()
        rport = entryAry[1].get()
        lport = entryAry[2].get()
        udpserv.update(int(lport) , rip , int(rport) , main_edit)
        udpserv.cnt()

    elif(udpserv.connect == 1):
        
        udpserv.cnt()

# 清除主 frame
def clean_main(main_edit):
    for widget in main_edit.winfo_children():
        widget.grid_remove()

def resume_CntPage():
    for widget in CntPage:
        widget.grid()

# 實時測試頁面配置
def open_viz(main_edit):

    clean_main(main_edit)