#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:33:24 2020

@author: caitlin
"""
import numpy as np
import math as math
import matplotlib as plt
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


G_dB=np.linspace(0.001, 30, 100)
G=10**(G_dB/10)
Y=np.exp(-(G-1)/10)
diff=abs(Y-G/1000)
int_G_dB=G_dB[np.argmin(diff)]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('G, dB')
ax1.set_ylabel('exp(-(G-1)/10)', color=color)
ax1.set_ylim([1e-4,1])
ax1.plot(G_dB, Y, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_yscale('log')
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('G/1000', color=color)  # we already handled the x-label with ax1
ax2.plot(G_dB, G/1000, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_yscale('log')
ax2.set_ylim([1e-4,1])
ax2.axvline(x=int_G_dB, color="green", label="Intercept", linestyle="dashed")
ax2.axhline(y=Y[np.argmin(diff)], color="green",linestyle="dashed")
ax2.set_xlim([0,30])

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.grid()
plt.show()

print("Gain (dB) at intersection="+str(int_G_dB))
normal_G=10**(int_G_dB/10)
print("Gain, norm fraction: "+str(normal_G))
p_out=1e-3*normal_G
print("Outpower, mW="+str(p_out*1000))

         

#%%





    
