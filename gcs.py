import tkinter as tk
import functools
from tkinter import *
from functools import partial
from DroneWt import *
from postPage import *
from cntPage import *
from rtosPage import *
from net import *
from plot import *

class GCS():

    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("地面站")

        # 視窗最小長寬
        self.window.rowconfigure(0, minsize=800, weight=1)
        self.window.columnconfigure(1, minsize=800, weight=1)

        # 主版面配置
        self.main_edit = tk.Frame(self.window)

        # 選項版面配置
        self.fr_buttons = tk.Frame(self.window, relief=tk.RAISED, bd=1)
        self.btn_cnt = tk.Button(self.fr_buttons, text="飛控連接", command=partial(open_cnt , self.main_edit)) # 按下後顯示飛控連接頁面
        self.btn_post = tk.Button(self.fr_buttons, text="飛控姿態", command=partial(open_post , self.main_edit)) # 按下後顯示飛控姿態寫入頁面
        self.btn_viz = tk.Button(self.fr_buttons, text="實時測試", command=partial(open_rtos , self.main_edit)) # 按下後顯示實時測試頁面
        self.btn_cnt.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.btn_post.grid(row=1, column=0, sticky="ew", padx=5 , pady=5)
        self.btn_viz.grid(row=2, column=0, sticky="ew", padx=5 , pady=5)

        # 全版面配置
        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        self.main_edit.grid(row=0, column=1, sticky="nsew")

gcs = GCS()

if __name__ == '__main__':

    # gcs.window.after(10 , functools.partial(DronePlot, gcs))
    
    # 初始化頁面
    open_cnt(gcs.main_edit)
    open_post(gcs.main_edit)
    open_rtos(gcs.main_edit)

    gcs.window.mainloop()
    

