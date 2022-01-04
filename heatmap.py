# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:02:29 2021

@author: u0128847
"""
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

class snapshots:
    def __init__(self):
        self.fig, self.ax = plt.subplots(2,2)
    def plot(self,T,dt):
        k = 0
        sz = np.shape(T)
        for a in self.ax:
            for b in a:
                k+=1
                it = int(sz[0]*k/4)-1
                im = b.imshow(np.floor(T[it]), interpolation='nearest', 
                                    origin='bottom', 
                                    aspect='auto', # get rid of this to have equal aspect
                                    vmin=np.min(T[it]),
                                    vmax=np.max(T[it]), 
                                    cmap='jet')  
                b.set_title("Temperature map t = {:.2f} s".format(it*dt))  
        self.fig.colorbar(im)
class heatmap:
    def __init__(self,u0):
         self.fig, self.ax = plt.subplots()
         self.im = self.ax.imshow(u0, interpolation='nearest', 
                            origin='bottom', 
                            aspect='auto', # get rid of this to have equal aspect
                            vmin=np.min(u0),
                            vmax=np.max(u0), 
                            cmap='jet')
         self.cb = self.fig.colorbar(self.im)
         self.ax.set_title("Temperature map t = 0 s")

    def update(self,u,t):
        self.im.set_data(u)
        self.ax.set_title("Temperature map t = {:.2f} s".format(t))
        display(self.fig)
    
        