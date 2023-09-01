#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	DESCRIÇÃO: AVALIAÇÃO DO ERRO GLOBAL (da integração numérica)
    Use a integração numérica do problema do oscilador massa-mola
    
                        d2x/(dt**2) = ((-w)**2)*x
                        
    para determinar o erro global do método de Runge-Kutta do ponto médio.
    Comece cada integração com x0=1., v0=0, w=1. e use como solução analítica
    x=cos(wt) e v=-w sin(wt).

    Note que esse problema é uma EDO de segunda ordem, portanto, deve ser
    calculado o erro para a posição e para a velocidade.
     
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
        http://www.if.ufrgs.br/tex/metcompb/
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		O erro global seria a diferença entre a solução analítica e a numérica
        no tempo final.
        
	VERSÃO:
	0.01 - 19/01/2023 

"""
#%%

import numpy as np
import matplotlib.pyplot as plt

w = 1.
x0 = 1.
v0 = 0.
A = 40.
tf = 24.
t = 0.
deltaT = dt0 = 10**(-5)

errox = 0.
errov = 0.

listaX = [errox]
listaV = [errov]
listaD = [deltaT]

def fx(v):
  return v

def fv(x):
  return (-w**2)*np.sin(x)

def analiticoX(x):
    return np.cos(w*t)

def analiticoV(v):
    return (-w)*np.sin(w*t)

def rungekutta(x, v, deltaT, w = 1):
    
    k1x = fx(v)
    k1v = fv(x)
  
    xaux = x + k1x * (deltaT/2)
    vaux = v + k1v * (deltaT/2)
  
    k2x = fx(vaux)
    k2v = fv(xaux)
  
    x = x + k2x * deltaT
    v = v + k2v * deltaT
    
    return x, v
    
while deltaT < 1:
    
    deltaT = 2*deltaT
    x = x0
    v = v0
    t = 0 
    
    while t < tf:
        
        x, v = rungekutta(x, v, deltaT)
        errox += x - A* np.cos(w)*t
        errov += v + A*w* np.sin(w*t)
        t += deltaT
        
        listaX.append(np.log10(np.abs(errox)))
        listaV.append(np.log10(np.abs(errov)))
        listaD.append(np.log10(deltaT))
        
   # print(np.log10(deltaT), np.log10(np.abs(errox)), np.log10(np.abs(errov)))
    
plt.plot(listaX, listaD   )
plt.xlabel('Velocidade')
plt.ylabel('Tempo')
plt.show()