#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    QUESTÃO 3 DA AVALIAÇÃO 1 - MÉTODO COMPUTACIONAIS DA FÍSICA B
    
    Utilizando método Euler-Cromer.
    
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	OBSERVAÇÕES:
	 
	VERSÃO:
	0.01 - 09/02/2023
"""
#%%

import numpy as np
import matplotlib.pyplot as plt 

# x representa a presa
# y representa o predador

#%% GRÁFICO: X = 1

y0 = 1
x0 = 1

x = x0
y = y0

w = 1
t = 0
tf = 8

deltaT = 0.05

listaX = [x]
listaY = [y]

while t < tf:
    xaux = x - x* y
    yaux = x*y - y
    
    x = x + y*deltaT
    y = y - ((w**2)* np.sin(x))*deltaT
    t += deltaT
  
    listaX.append(x)
    listaY.append(y)

plt.plot(listaX, listaY, label = "x = 1")
plt.legend(loc = 10)
plt.title("Gráfico 1 - Espaço de Fases")
plt.show()
  
#%% GRÁFICO X = 1.5

y0 = 1
x0 = 1.5

x = x0
y = y0

w = 1
t = 0
tf = 8

deltaT = 0.05

listaX = [x]
listaY = [y]

def lotka(x, y, deltaT):
    x= x- x *y
    y = x * y - y
    return 

while t < tf:
    xaux = x - x* y
    yaux = x*y - y
    
    x = x + y*deltaT
    y = y - ((w**2)* np.sin(x))*deltaT
    t += deltaT
  
    listaX.append(x)
    listaY.append(y)
  
plt.plot(listaX, listaY, label = "x = 1.5", color = 'magenta')
plt.legend(loc = 10)
plt.title("Gráfico 2 - Espaço de Fases")
plt.show()

#%% GRÁFICO X = 2

y0 = 1
x0 = 2

x = x0
y = y0

w = 1
t = 0
tf = 8

deltaT = 0.05

listaX = [x]
listaY = [y]

while t < tf:
    xaux = x - x* y
    yaux = x*y - y
    
    x = x + y*deltaT
    y = y - ((w**2)* np.sin(x))*deltaT
    t += deltaT
   
    listaX.append(x)
    listaY.append(y)
    
plt.plot(listaX, listaY, label = "x = 2", color = 'red')
plt.legend(loc = 10)
plt.title("Gráfico 3 - Espaço de Fases")
plt.show()

#%% GRÁFICO X = 2.5

y0 = 1
x0 = 2.5

x = x0
y = y0

w = 1
t = 0
tf = 8

deltaT = 0.05

listaX = [x]
listaY = [y]

while t < tf:
    xaux = x - x* y
    yaux = x*y - y
    
    x = x + y*deltaT
    y = y - ((w**2)* np.sin(x))*deltaT
    t += deltaT
   
    listaX.append(x)
    listaY.append(y)
  
plt.plot(listaX, listaY, label = "x = 2.5", color = 'green')
plt.legend(loc = 10)
plt.title("Gráfico 4 - Espaço de Fases")
plt.show()

#%% GRÁFICO X = 3

y0 = 1
x0 = 3

x = x0
y = y0

w = 1
t = 0
tf = 8

deltaT = 0.05

listaX = [x]
listaY = [y]

while t < tf:
    xaux = x - x* y
    yaux = x*y - y
    
    x = x + y*deltaT
    y = y - ((w**2)* np.sin(x))*deltaT
    t += deltaT
   
    listaX.append(x)
    listaY.append(y)
  
plt.plot(listaX, listaY, label = "x = 3", color = 'purple')
plt.legend(loc = 10)
plt.title("Gráfico 5 - Espaço de Fases")
plt.show()
