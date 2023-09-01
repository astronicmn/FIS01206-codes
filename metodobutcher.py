#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	DESCRIÇÃO:
      
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		
	VERSÃO:
	0.01 - 22/12/2022
"""

#%% 
import numpy as np
import matplotlib.pyplot as plt

#%%

x0 = 1
v0 = 0
w0 = 1
w = 1.1
x = x0
v = v0
tf = 24
t = 0
deltaT = 0.1
r = 10

a = [0.1, 0.5, 1]

listaX = [x0]
listaT = [0]
listaV = [v0]

def fx(v):
    return v
   
def fv(t,x):
    return -(w0**2)*np.sin(x) + a[1]*np.sin(w*t)    
    
while t < tf:
    
    k1x = fx(v)
    k1v = fv(t, x)
    
    xaux = x + k1x*(deltaT/2)
    vaux = v + k1v*(deltaT/2)
    
    k2x = fx(vaux)
    k2v = fv(t + (deltaT/2), xaux)
    
    x = x + k2x*deltaT
    v = v + k2v*deltaT
    
    xaux = x + k2x*(deltaT/2)
    vaux = v + k2v*(deltaT/2)
    
    k3x = fx( vaux)
    k3v = fv(t + (deltaT/2), xaux)
    
    xaux = x + k2x*deltaT
    vaux = v + k2v*deltaT
    
    k4x = fx(v)
    k4v = fv(t + deltaT, xaux)
    
    x = x + (deltaT/6)*(k1x + 2*k2x + 2*k3x + k4x)
    v = v + (deltaT/6)*(k1v + 2*k2v + 2*k3v + k4v)
    
    t += deltaT

    listaX.append(x)
    listaT.append(t)
    listaV.append(v)
    
plt.plot(listaT, listaX, color = 'b', label = 'Butcher')
plt.show()
