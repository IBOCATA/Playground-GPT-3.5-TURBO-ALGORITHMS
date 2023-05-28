# -*- coding: utf-8 -*-
"""
Created on Sun May 21 11:31:05 2023

@author: ilias
"""

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint 

 # define the initial concentration of pesticide in the reservoir 
C0 = 0.2 # mg/L

 # define diffusivity and convection coefficient for pesticide in water 
D = 2e-9 # m2/s  
V = 1e-6 # m/s  

 # define length and width of reservoir (m) 
Lx, Ly = 100, 50  

 # grid size (m) - dx is space between x points, dy is space between y points   
dx, dy = 10, 5  

 # define grid 
x = np.arange(0, Lx + dx, dx)  
y = np.arange(0, Ly + dy, dy)  

 # create meshgrid 
X, Y = np.meshgrid(x, y) 


 # calculate Concentration of pesticide in the reservoir after applying phytoremediation (mg/L) 
def concentration_reservoir(C0):     

     def f_diffconvect(c,t):
         dc_dx2 = (np.roll(c,-1)+np.roll(c,1)-2*c)/dx**2         
         dc_dy2 = (np.roll(c,-1)+np.roll(c,1)-2*c)/dy**2         
         dc_dx = np.diff(c, axis=0) / dx         
         dc_dy = np.diff(c, axis=1) / dy                 

        # convection-diffusion equation         
         dcdt = D * (dc_dx2 + dc_dy2) - V * (dc_dx + dc_dy)          

        # boundary conditions 
         dcdt[:, 0] = 0  # zero gradient at x boundaries          
         dcdt[:, -1] = 0  # zero gradient at y boundaries     

         # return the concentration of pesticide in reservoir     
         return dcdt 
     t = np.linspace(0, 1000, 10000)   # define time range (s) 
    
     C = odeint(f_diffconvect, C0, t)

    # reshape to 2D array and plot     
     plt.contourf(X, Y, np.reshape(C[-1], X.shape))     
     plt.title('Phytoremediation for Hydrogeological Reservoir Pollution by Pesticide')       
     plt.xlabel('Length (m)')       
     plt.ylabel('Width (m)')      
     plt.colorbar()     
     plt.show() 
concentration_reservoir(C0)