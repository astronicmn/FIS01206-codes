#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    MÉTODO PASSO VARIÁVEL utilizado em problemas onde há variações
    em larga escala nas derivadas.
    
    PROBLEMA PÊNDULO SIMPLES:
    
    Use os métodos RK2 (ponto médio) e RK4 (clássico) para implementar um 
    método de passo variável para o problema do pêndulo simples com estímulo
    externo. Use as condições iniciais e de estímulo implementadas nos 
    problemas anteriores.
        
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		
	VERSÃO:
	0.01 - 24/01/2023

"""
#%%

import numpy as np
import matplotlib.pyplot as plt

x0 = 0.1
v0 = 0

w0 = 1
w = 0.5

A = 0

x = x0
v = v0

x_list = [x]
v_list = [v]
t_list = [0]
deltaT_list = [.1]

a = [0.1, 0.5, 1] 

def fx(v):
  return v

def fv(t,x):
  return -(w0**2)*np.sin(x) + a[1]*np.sin(w*t)

def RK2(x, v, deltaT, t):
    
    k1x = fx(v)
    k1v = fv(t, x)
  
    xaux = x + k1x * (deltaT/2)
    vaux = v + k1v * (deltaT/2)
  
    k2x = fx(vaux)
    k2v = fv(t, xaux)
  
    x = x + k2x * deltaT
    v = v + k2v * deltaT
    
    return x, v

def RK4(x, v, deltaT, t):
    
    k1x = fx(v)
    k1v = fv(t,x)
  
    xaux = x + k1x * (deltaT/2)
    vaux = v + k1v * (deltaT/2)
    k2x = fx(vaux)
    k2v = fv(t + (deltaT/2), xaux)
  
    x = x + k2x * deltaT
    v = v + k2v * deltaT
  
    xaux = x + k2x * (deltaT/2)
    vaux = v + k2v * (deltaT/2)
    k3x = fx(vaux)
    k3v = fv(t + (deltaT/2), xaux)
  
    xaux = x + k3x * (deltaT)
    vaux = v + k3v * (deltaT)
    k4x = fx(vaux)
    k4v = fv(t + deltaT, xaux)
  
    x = x + (deltaT/6)*(k1x + 2*k2x + 2*k3x + k4x)
    v = v + (deltaT/6)*(k1v + 2*k2v + 2*k3v + k4v)
    t += deltaT
    
    return x, v

tf = 20
t = 0
tol = 10**(-2)
deltaT = .1
count = 0
limit_count = 10

while t < tf:
    
    count += 1
    xa, va = x, v
    t+= deltaT
    x, v = RK2(x, v, deltaT, t)
    
    if count%limit_count == 0:
        xp, vp = RK4(x, v, deltaT, t)
        Ecx = np.abs(x - xp)
        Ecv = np.abs(v - vp)
        Ec = np.max([Ecx, Ecv])
        
        deltaTnovo = deltaT*(tol/Ec)**1/3
        
        if deltaTnovo > 2*deltaT: deltaT = 2*deltaT
        
        if deltaTnovo < deltaT/2 : deltaT = deltaT/2
        
    x_list.append(x)
    v_list.append(v)
    t_list.append(t)
    deltaT_list.append(deltaT)

#%%
    
plt.plot(t_list, deltaT_list)
plt.xlabel('Tempo')
plt.ylabel('Delta T')

#%%

plt.plot(t_list, x_list)
plt.xlabel('Tempo')
plt.ylabel('X')

#%%
plt.plot(t_list, v_list)
plt.xlabel('Tempo')
plt.ylabel('V')

#%%

plt.plot(x_list, v_list, color = 'magenta')
plt.xlabel('X')
plt.ylabel('V')