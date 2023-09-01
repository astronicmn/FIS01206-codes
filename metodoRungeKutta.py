#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    MÉTODOS RUNGE - KUTTA (PONTO MÉDIO)
    
    São uma família de métodos iterativos explícitos e implícitos usados
    para a solução discretizada de equações diferenciais do tipo:
                          dt = f(x, t)
                          
    Usando o método de Runge-Kutta do ponto médio para integrar numéricamente 
    o problema do pêndulo simples.
    
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
	 
	VERSÃO:
	0.01 - 13/12/2022
"""
#%% Importando módulos:

import numpy as np
import matplotlib.pyplot as plt
#%% Utilizando dados do pêndulo simples. Gráfico de X x t --> Item 1:

# MÉTODO RUNGE-KUTTA: podemos observar que este método não é adequado para 
#                     ordens altas.

x0 = 3 
v0 = 0
w = 1
L = 10
g = 10
tf = 24
t = 0
deltaT = 0.5 
x = x0
v = v0

listaX = [x0]
listaT = [0]

def fx(v):
  return v

def fv(x):
  return (-w**2)*np.sin(x)

while t < tf:
  
  k1x = fx(v)
  k1v = fv(x)
  
  xaux = x + k1x * (deltaT/2)
  vaux = v + k1v * (deltaT/2)
  
  k2x = fx(vaux)
  k2v = fv(xaux)
  
  x = x + k2x * deltaT
  v = v + k2v * deltaT

  t += deltaT
  
  listaX.append(x)
  listaT.append(t)
  
plt.plot(listaT, listaX, color = 'magenta', label = "Runge-Kutta")

# MÉTODO VELOCITY-VERLET

x0 = 3
v0 = 0
w = 1
L = 10
g = 10
tf = 24
t = 0
deltaT = 0.5
x = x0
v = v0

listaX = [x0]
listaT = [0]

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaT.append(t)
  
plt.plot(listaT, listaX, color = 'b', label = "Velocity-Verlet")

plt.legend(loc=10)
#%% Gráfico do espaço de fases X x v --> Item 3:

# MÉTODO RUNGE-KUTTA

x0 = 1.0
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

def fx(v):
  return v

def fv(x):
  return (-w**2)*np.sin(x)

while t < tf:
  
    k1x = fx(v)
    k1v = fv(x)
  
    xaux = x + k1x * (deltaT/2)
    vaux = v + k1v * (deltaT/2)
  
    k2x = fx(vaux)
    k2v = fv(xaux)
  
    x = x + k2x * deltaT
    v = v + k2v * deltaT

    t += deltaT
    
    listaX.append(x)
    listaV.append(v)
    
plt.plot(listaV, listaX, color = 'magenta', label = 'Runge-Kutta')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

# MÉTODO VELOCITY-VERLET 

x0 = 1.0
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

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaV.append(v)

plt.plot(listaV, listaX, label = 'Velocity-Verlet')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

plt.legend(loc = 10)