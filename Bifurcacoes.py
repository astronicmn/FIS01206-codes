#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Diagrama de Bifurcações do Mapa Logístico

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
	0.01 - 28/02/2023
"""

#%%
import matplotlib.pyplot as plt 

def f(da, a):
    x_list = []
    a_list = []

    while (a<=4):        
        x = 0.7

        for i in range(0, 1000):
            x = a*x*(1-x)

        for i in range(0, 100):
            x = a*x*(1-x)
            x_list.append(x)
            a_list.append(a)

        a += da
    
    plt.scatter(a_list, x_list, s=0.6)
        
    plt.xlabel(r"$\lambda$")
    plt.ylabel(r"x")    
    plt.show()

f(0.01, 0)
f(0.001, 3)
f(0.001, 3)