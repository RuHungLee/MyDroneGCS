import tkinter as tk
import numpy as np
import time
import threading
from postPage import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib import animation, figure
from DroneWt import DS

class DroneViz():
    
    def __init__(self):
 
        self.ax = None
        self.ax2 = None
        self.ax3 = None
        self.ax4 = None
        self.ax5 = None
        self.ax6 = None
        self.xs1 = None
        self.ys1 = None
        self.line1 = None
        self.cnt = None
        self.ani = None

    def update(self , x , y , dpi , frame):
 
        fig = figure.Figure(figsize=(x, y), dpi=dpi , facecolor = '#f2f2f2')
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.get_tk_widget().grid(column=0, row=0)
        self.ax = fig.add_subplot(2, 3, 1)
        self.ax.set_title('ROLL')
        self.ax.set_ylim([-45 , 45])
        self.ax2 = fig.add_subplot(2, 3, 2)
        self.ax2.set_title('PITCH')
        self.ax2.set_ylim([-45 , 45])
        self.ax3 = fig.add_subplot(2, 3, 3)
        self.ax3.set_title('YAW')
        self.ax3.set_ylim([-45 , 45])
        self.ax4 = fig.add_subplot(2, 3, 4)
        self.ax4.set_ylim([-45 , 45])
        self.ax5 = fig.add_subplot(2, 3, 5)
        self.ax5.set_ylim([-45 , 45])
        self.ax6 = fig.add_subplot(2, 3, 6)
        self.ax6.set_ylim([-45 , 45])
        self.xs1 = np.arange(0 , 300 , 1)
        self.ys1 = np.zeros(300)
        self.line1 , = self.ax.plot(self.xs1 , self.ys1)
        self.xs2 = np.arange(0 , 300 , 1)
        self.ys2 = np.zeros(300)
        self.line2 , = self.ax2.plot(self.xs2 , self.ys2)
        self.xs3 = np.arange(0 , 300 , 1)
        self.ys3 = np.zeros(300)
        self.line3 , = self.ax3.plot(self.xs3 , self.ys3)

        self.cnt = 0
        self.ani = animation.FuncAnimation(fig, self.run , np.arange(1, 300) , interval=30 , blit=True)

    def run(self , i):
        self.line1.set_ydata(DS.roll)
        self.line2.set_ydata(DS.pitch)
        self.line3.set_ydata(DS.yaw)
        return self.line1 , self.line2 , self.line3 ,

DV = DroneViz()