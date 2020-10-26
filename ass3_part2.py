#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:34:15 2020

@author: caitlin
"""
import numpy as np
import math as math
import matplotlib as plt
import matplotlib.pyplot as plt


n2=3.2e-23*1e3 #m^2/W
wavelength=1550e-9 #m
P_in=np.linspace(0,100,100000) #input power, 1 to 100 W
core_rad=2.5e-6 #m
core_area=np.pi*core_rad**2
overlap=2

I_in=overlap*P_in/(core_area) #w/m^2

def I_out(I_in, a, L_f):
    I_out=(I_in*G*(1-2*a*(1-a)*(1+np.cos(I_in*2*np.pi*n2*L_f*(a-G*(1-a))/wavelength))))
    return I_out

G=1 #for NOLM

plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.49,  200)/overlap, label=r"L=200")
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.49,  800)/overlap, label=r"L=800")
plt.xlim(0,max(P_in))
plt.xlabel("Input power, W")
plt.ylabel("Output power, W")
plt.legend()
plt.title(r"NOLM, $\alpha$=0.49")
plt.grid()
plt.show()

plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.48, 200)/overlap, label=r"L=200")
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.48, 800)/overlap, label=r"L=800")
plt.xlim(0,max(P_in))
plt.xlabel("Input power, W")
plt.ylabel("Output power, W")
plt.legend()
plt.grid()
plt.title(r"NOLM, $\alpha$=0.48")
plt.show()


plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.80,  200)/overlap, label=r"L=200")
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.80,  800)/overlap, label=r"L=800")
plt.xlim(0,max(P_in))
plt.xlabel("Input power, W")
plt.ylabel("Output power, W")
plt.legend()
plt.grid()
plt.title(r"NOLM, $\alpha$=0.8")
plt.show()


#%%  Question 2
L_f=10
L_a=10

def L_from_alpha(P_in, alpha):
    L=0.5*wavelength*core_area/(n2*P_in*overlap*abs(2*alpha-1))
    return L

a_1=0.45
L_1=L_from_alpha(100,a_1 )
print(L_1)
a_2=0.25
L_2=L_from_alpha(100,a_2 )
print(L_2)

a_3=0.05
L_3=L_from_alpha(100,a_3 )
print(L_3)

plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  a_1,  L_1)/overlap, label=r"$\alpha=$"+str(a_1)+", L="+str(round(L_1,3)) )
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  a_2,  L_2)/overlap, label=r"$\alpha=$"+str(a_2)+", L="+str(round(L_2,3)) )
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  a_3,  L_3)/overlap, label=r"$\alpha=$"+str(a_3)+", L="+str(round(L_3,3)) )

plt.xlim(0,max(P_in))
plt.xlabel("Input power, W")
plt.ylabel("Output power, W")
plt.legend()
plt.grid()
plt.title(r"NOLM optimised for a pulse train, examples")
plt.show()

#%% Question 3 Whats going on   #appraching from different alphas  perfectly deconstructive, 180 out of phase
L_f=100   #generic fibre length
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.4, L_f)/overlap, label=r"$\alpha$="+str(0.4))
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.45, L_f)/overlap, label=r"$\alpha$="+str(0.45))
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.49, L_f)/overlap, label=r"$\alpha$="+str(0.49))
plt.plot(I_in*core_area/overlap, core_area*I_out(I_in,  0.5, L_f)/overlap, label=r"$\alpha$="+str(0.5))

plt.xlim(0,max(P_in))
plt.xlabel("Input power")
plt.ylabel("Output power")
plt.legend()
plt.grid()
plt.title(r"NOLM, L=100m for $\alpha$ approaching 0.5")
plt.show()


#%% Question 4 

n2=3.2e-23*1e3 #m^2/W
wavelength=1550e-9 #m

L_a=10 #m  #length of amplifier
     
g_0=1.56
I_s=0.49*1e-3*(overlap/core_area) #W
P_in=np.linspace(0.000001,0.4*1e-3,10000) #input power, 0 to 0.4mW
core_rad=2.5e-6 #m
core_area=np.pi*core_rad**2
L_f=35
a=0.5

overlap=2
I_in=overlap*P_in/(core_area) #w/m^2

def G_f(g_0, I_s, I_in):  #function to work out amp gain
    g=(g_0*I_s/(I_in+I_s))
    G=np.exp(g*L_a)
    return G

def I_out(I_in, G):   #function to determine I out from I in
    I_out=(I_in*G*(1-2*a*(1-a)*(1+np.cos(I_in*2*np.pi*n2*L_f*(a-G*(1-a))/wavelength))))
    return I_out 

G_amp=G_f(g_0, I_s, I_in)    #gain of amp

I_out_amp=I_out(I_in, G_amp)
P_out_amp=core_area*I_out_amp/overlap

G_overall=P_out_amp/P_in

plt.plot(P_in*1000, 10*np.log10(G_amp), label="Gain of amplifier")
plt.ylabel("G(dB)")
plt.xlabel(r"$P_{in}$, mW")
plt.title("Gain as a function of input power")
plt.plot(P_in*1000, 10*np.log10(G_overall), label="Gain of NALM")
plt.grid()
plt.legend()
plt.show()

plt.plot(P_in*1000, P_out_amp)
plt.plot(P_in*1000, P_in)
plt.ylabel("Transmitted power, W")
plt.xlabel(r"$P_{in}$, mW")
#plt.yscale("log")
plt.title("Output power as function of input power")
plt.grid()
plt.show()

#plt.xlim(0,0.4*1e-3)
