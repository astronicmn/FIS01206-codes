#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Pêndulo Simples - Velocity-Verlet
    
	DESCRIÇÃO:
		Use o método de Verlet para integrar numéricamente o problema
        do pêndulo simples. Compare as soluções com o método de Verlet.
        
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		Para tornar executável:
		% chmod ugo+x <nome_do_programa>
		
		Para criar um link em ~/bin:
		% ln ~/prog/python/programa.py> ~/bin/<programa>
	 
	VERSÃO:
	0.01 - 08/12/2022
"""
#%% Importando módulos:

import numpy as np
import matplotlib.pyplot as plt

#%% POSIÇÃO PÊNDULO x TEMPO

x0 = 0.5
v0 = 0
w = 1
L = 10
g = 10
tf = 24
t = 0
deltaT = 0.1
x = x0
v = v0

listaX = [x0]
listaT = [0]

xaux = x

while t < tf:
  
  xaux = x
  x = x + (v*deltaT) - 1/2 *((w**2)*np.sin(x))*(deltaT**2)
  v = v - (w**2)*(np.sin(x)/2 + np.sin(xaux)/2)*deltaT
  t += deltaT
  
  listaX.append(x)
  listaT.append(t)

plt.plot(listaT, listaX)
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Posição do Pêndulo')

#%% POSIÇÃO PÊNDULO x VELOCIDADE 

x0 = 3.0
v0 = 0
w = 1
L = 10
g = 10
tf = 24
t = 0
deltaT = 0.1
x = x0
v = v0

listaX = [x0]
listaV = [v0]
listaT = [0]

xaux = x

while t < tf:
  
  xaux = x
  
  x = x + (v*deltaT) - 1/2 *((w**2)*np.sin(x))*(deltaT**2)
  v = v - (w**2)*(np.sin(x)/2 + np.sin(xaux)/2)*deltaT
  t += deltaT

  listaX.append(x)
  listaV.append(v)
  listaT.append(t)
  
plt.plot(listaT, listaV)
plt.grid(True, linestyle='--')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

#%% ENERGIA x TEMPO

x0 = 3 * 3.14159
v0 = - 0.1
w = 1
L = 10
g = 10
tf = 24
t = 0
deltaT = 0.1
x = x0
v = v0
m = 1
Ec = 0
Ep = 0 
Et = 0
xaux = 0
omega = g/L

listaEp = []
listaEc = []
listaEt = []
listaT = [0]
xaux = x
while t < tf:
    
    xaux = x
    x0 = x
    t += deltaT
    
    x = x + (v*deltaT) - 1/2 *((w**2)*np.sin(x))*(deltaT**2)
    v = v - ((w**2)*np.sin(x)/2)*deltaT
    t += deltaT
    
    Ec = (1/2)* m*((L**2)*(v**2))
    Ep = m*g*L*(1 - np.cos(x))
    Et = Ec + Ep
    
    listaT.append(t)
    listaEp.append(Ep)
    listaEc.append(Ec)
    listaEt.append(Et)
    
del listaT[-1]
plt.plot(listaT, listaEc, label = 'Energia Cinética')
plt.plot(listaT, listaEp, label = 'Energia Potencial')
plt.plot(listaT, listaEt, label = 'Energia Total!', color = 'cyan')
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Energia')

plt.legend(loc = 10)