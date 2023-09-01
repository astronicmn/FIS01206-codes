#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Problema do Pêndulo Simples
    
	DESCRIÇÃO:
		Usando o método de Euler-Cromer, escreva um programa que integre 
        numericamente  o problema do pêndulo simples a partir de condições 
        iniciais x0 e v0. Faça um relatório (latex) para colocar o problema, 
        descrever o método e colocar conclusões onde interpreta os resultados
        encontrados.

	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
	
	BUGS/LIMITAÇÕES:

	ToDos:
	
	OBSERVAÇÕES:
	 
	VERSÃO:
	0.01 - dezembro/2022
    
"""
#%% Importando módulos:

import matplotlib.pyplot as plt
import numpy as np

#%% Gráficos de X x t para os ítens 1, 2, 3 e 4.

# Item 1:

x0 = 0.1
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

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaT.append(t)
  
plt.plot(listaT, listaX, color = 'magenta', label = "Item 1")

# Item 2:

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
listaT = [t]

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaT.append(t)

plt.plot(listaT, listaX, color = 'r', label = "Item 2")

# Item 3:

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
listaT = [t]

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaT.append(t)

plt.plot(listaT, listaX, color = 'g', label = "Item 3")

# Item 4:

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
listaT = [t]

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaT.append(t)

plt.plot(listaT, listaX, label = "Item 4")

plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Posição do Pêndulo')

plt.legend(loc = 1)
#%% Gráficos do espaço de fases X x v

# Item 1:

x0 = 0.1
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

plt.title("Item 1: v0 = 0 | x0 = 0.1")
plt.plot(listaV, listaX, color = 'magenta')
plt.grid(True, linestyle='--')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

#%% Item 2: 

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
listaV = [v0]

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaV.append(v)

plt.title("Item 2: v0 = 0 | x0 = 0.5")
plt.plot(listaV, listaX, color = 'r')
plt.grid(True, linestyle='--')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

#%% Item 3:

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

plt.title("Item 3: v0 = 0 | x0 = 1.0")
plt.plot(listaV, listaX, color = 'g')
plt.grid(True, linestyle='--')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

#%% Item 4:

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

while t < tf:
  x = x + v*deltaT
  v = v - ((w**2)* np.sin(x))*deltaT
  t += deltaT
  
  listaX.append(x)
  listaV.append(v)

plt.title("Item 4: v0 = 0 | x0 = 3.0")
plt.plot(listaV, listaX)
plt.grid(True, linestyle='--')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

#%% Item 5:

x0 = 3 * 3.14159
v0 = -0.1
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

plt.plot(listaV, listaX,'c--', label = "v0 = -0.1 | x0 = 3*3.14159")
plt.grid(True, linestyle='--')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

# Item 6:

x0 = - 3 * 3.14159
v0 = 0.1
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

plt.plot(listaV, listaX,'m-', label = "v0 = 0.1 | x0 = -3*3.14159")
plt.grid(True, linestyle='--')
plt.xlabel('Velocidade')
plt.ylabel('Posição do Pêndulo')

plt.title("Itens 5 e 6")
plt.legend(loc = 10)

#%% Gráficos Energia Total

# Item 1:

x0 = 0.1
v0 = 0
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

while t < tf:
    
    xaux = x
    x0 = x
    t += deltaT
    
    v = v - omega * np.sin(x) * deltaT
    x = x + v*deltaT
    
    Ec = (1/2)* m*((L**2)*(v**2))
    Ep = m*g*L*(1 - np.cos(x))
    Et = Ec + Ep
    
    listaT.append(t)
    listaEp.append(Ep)
    listaEc.append(Ec)
    listaEt.append(Et)
    
del listaT[-1]
#plt.plot(listaT, listaEc, label = 'Energia Cinética')
#plt.plot(listaT, listaEp, label = 'Energia Potencial')
plt.plot(listaT, listaEt, label = 'Energia Total!', color = 'magenta')
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Energia')


plt.title("Item 1: v0 = 0 | x0 = 0.1")
plt.legend(loc = 10)
#%% Item 2:

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

while t < tf:
    
    xaux = x0
    x0 = x
    t += deltaT
    
    v = v - omega * np.sin(x) * deltaT
    x = x + v*deltaT
    
    Ec = (1/2)* m*((L**2)*(v**2))
    Ep = m*g*L*(1 - np.cos(x))
    Et = Ec + Ep
    
    listaT.append(t)
    listaEp.append(Ep)
    listaEc.append(Ec)
    listaEt.append(Et)
    
del listaT[-1]
#plt.plot(listaT, listaEc, label = 'Energia Cinética')
#plt.plot(listaT, listaEp, label = 'Energia Potencial')
plt.plot(listaT, listaEt, label = 'Energia Total!', color = 'r')
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Energia')


plt.title("Item 2: v0 = 0 | x0 = 0.5")
plt.legend(loc = 10)
#%% Item 3:

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

while t < tf:
    
    xaux = x0
    x0 = x
    t += deltaT
    
    v = v - omega * np.sin(x) * deltaT
    x = x + v*deltaT
    
    Ec = (1/2)* m*((L**2)*(v**2))
    Ep = m*g*L*(1 - np.cos(x))
    Et = Ec + Ep
    
    listaT.append(t)
    listaEp.append(Ep)
    listaEc.append(Ec)
    listaEt.append(Et)
    
del listaT[-1]
#plt.plot(listaT, listaEc, label = 'Energia Cinética')
#plt.plot(listaT, listaEp, label = 'Energia Potencial')
plt.plot(listaT, listaEt, label = 'Energia Total!', color = 'lime')
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Energia')


plt.title("Item 3: v0 = 0 | x0 = 1.0")
plt.legend(loc = 10)
#%% Item 4:

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

while t < tf:
    
    xaux = x0
    x0 = x
    t += deltaT
    
    v = v - omega * np.sin(x) * deltaT
    x = x + v*deltaT
    
    Ec = (1/2)* m*((L**2)*(v**2))
    Ep = m*g*L*(1 - np.cos(x))
    Et = Ec + Ep
    
    listaT.append(t)
    listaEp.append(Ep)
    listaEc.append(Ec)
    listaEt.append(Et)
    
del listaT[-1]
#plt.plot(listaT, listaEc, label = 'Energia Cinética')
#plt.plot(listaT, listaEp, label = 'Energia Potencial')
plt.plot(listaT, listaEt, label = 'Energia Total!', color = 'darkviolet')
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Energia')


plt.title("Item 4: v0 = 0 | x0 = 3.0")
plt.legend(loc = 10)
#%% Item 5:

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

while t < tf:
    
    xaux = x0
    x0 = x
    t += deltaT
    
    v = v - omega * np.sin(x) * deltaT
    x = x + v*deltaT
    
    Ec = (1/2)* m*((L**2)*(v**2))
    Ep = m*g*L*(1 - np.cos(x))
    Et = Ec + Ep
    
    listaT.append(t)
    listaEp.append(Ep)
    listaEc.append(Ec)
    listaEt.append(Et)
    
del listaT[-1]

#plt.plot(listaT, listaEc, label = 'Energia Cinética')
#plt.plot(listaT, listaEp, label = 'Energia Potencial')
plt.plot(listaT, listaEt, label = 'Energia Total!', color = 'cyan')
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Energia')


plt.title("Item 5: v0 = -0.1 | x0 = 3*3.14159")
plt.legend(loc = 10)
#%% Item 6:

x0 = - 3 * 3.14159
v0 = 0.1
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

while t < tf:
    
    xaux = x0
    x0 = x
    t += deltaT
    
    v = v - omega * np.sin(x) * deltaT
    x = x + v*deltaT
    
    Ec = (1/2)* m*((L**2)*(v**2))
    Ep = m*g*L*(1 - np.cos(x))
    Et = Ec + Ep
    
    listaT.append(t)
    listaEp.append(Ep)
    listaEc.append(Ec)
    listaEt.append(Et)
    
del listaT[-1]
#plt.plot(listaT, listaEc, label = 'Energia Cinética')
#plt.plot(listaT, listaEp, label = 'Energia Potencial')
plt.plot(listaT, listaEt, label = 'Energia Total!', color = 'b')
plt.grid(True, linestyle='--')
plt.xlabel('Tempo')
plt.ylabel('Energia')


plt.title("Item 6: v0 = 0.1 | x0 = -3*3.14159")
plt.legend(loc = 10)