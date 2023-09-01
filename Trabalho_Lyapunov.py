#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
     Diagrama de Bifurcações e Expoente de Lyapunovo

	AUTOR:
		N. M. Narvaz
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
		<[#] referência..>
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:

	VERSÃO:
	0.01 - 16/03/2023
"""
#%%

import matplotlib.pyplot as plt
import numpy as np

def f(x, a):
    return a*x*(1-x)

def df(x, a):
    return a - 2*a*x

a_list = np.linspace(3, 5, 4, 1000)

grafico = []
expoente = []
bifurca = []

for a in a_list:
    x = 0.7
    e = 0
    
    for i in range(900):
        e += np.log(abs(df(x, a)))
        x = f(x,a)
    x_list = []
    
    for i in range(100):
        e += np.log(abs(df(x, a)))
        x = f(x, a)
        x_list.append(x)
        
    expoente.append(e/1000)
    plt.scatter(a*np.ones(100), x_list,  s=0.01)
    if abs(e/1000) < 0.01:
        bifurca.append(a)
        
plt.scatter(a_list, expoente, s=5)

for i in bifurca:
    plt.plot(i*np.array((1,1)), [0,1])
    
plt.ylim(0,1)
plt.show()
