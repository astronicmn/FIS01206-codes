#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	DESCRIÇÃO:
		MÉTODO DE VERLET

	AUTOR:
		N. M. Narvaz
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
		fiscomp.if.ufrgs.br/index.php/M%C3%A9todo_de_Verlet
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
	 
	VERSÃO:
	0.01 - 06/12/2022
"""

#%% Importando módulos:

import matplotlib.pyplot as plt
import numpy as np        

#%% 

x0 = 0.1
v0 = 0
tf = 24
t = 0
deltaT = 0.1
w = 1
x = x0
v = v0
L = 10

listaX1 = [x0]
listaT = [0]
listaV = [v0]

xaux = x0 - v0*deltaT

while t < tf:
    x1 = 2*x - xaux - (w**2)*np.sin(x)*(deltaT**2)
    v = (x1 - xaux) / 2*deltaT
    
    xaux = x
    x = x1
    
    t +=deltaT
    
    listaX1.append(x1)
    listaT.append(t)
    listaV.append(v)
    
plt.plot(listaT, listaX1, color = 'magenta', label = "Oscilações Verlet")
plt.legend(loc = 1)
#plt.plot()


#%% DO IF
                 
#Constantes
m=1  ; k= 1.; w2= k/m

#Valores iniciais
x=[1]; v=[0]; t=[0] ; E=[k*(x[0]**2)/2+m*(v[0]**2)/2] 

#Parâmetros
dt  = 0.1 ; tau = 2*np.pi; tf=4*tau ; Np= int(tf/dt)

# Método de Euler-Cormer para obter o primeiro passo:

x.append(x[0]+dt*v[0])  
t.append(dt)

# Método de Verlet:
for it in range(1,Np):
  x.append(-w2*x[it]*dt*dt-x[it-1]+2*x[it]) #Método de Verlet
  v.append((x[it+1]-x[it-1])/(2*dt))
  E.append(k*x[it]**2/2+m*v[it]**2/2)
  t.append(dt+it*dt)

plt.plot(t,x)
plt.plot(t[:len(t)-1],v) #Velocidade tem um elemento a menos
plt.plot(t[:len(t)-1],E)
plt.plot(x[:len(x)-1],v)

# Método de Velocidade Verlet:

#Constantes
m=1  ; k= 1.; w2= k/m

#Valores iniciais
x=[1]; v=[0]; t=[0] ; E=[k*(x[0]**2)/2+m*(v[0]**2)/2] 

#Parâmetros
dt  = 0.1 ; tau = 2*np.pi; tf=4*tau ; Np= int(tf/dt)

for it in range(Np):
  x.append(x[it]+v[it]*dt-w2*x[it]*dt**2/2)
  v.append(v[it]+(-w2*x[it+1]-w2*x[it])*dt/2)
  E.append(k*x[it]**2/2+m*v[it]**2/2)
  t.append(dt+it*dt)

plt.plot(t,x)
plt.plot(t,v)
plt.plot(t,E)
plt.plot(x,v)