#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Bifurcação para o ciclo 2

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
	0.01 - 23/02/2023
"""
import matplotlib.pyplot as plt
import numpy as np

#%% Faça um gráfico de g(x) e da função identidade.  

a = 2.9
x = np.linspace(0 , 1 , 50)
g = a*(a*x*(1-x))*(1-(a*x*(1-x)))

#print(g)

plt.plot(x, g, 'r', label='a = 2.9')
plt.plot(x, x, 'k', label='identidade')

plt.legend()

#%%
a = 3.1
x = np.linspace(0 , 1 , 50)
g = a*(a*x*(1-x))*(1-(a*x*(1-x)))

#print(g)

plt.plot(x, g, 'r', label = 'a = 3.1')
plt.plot(x, x, 'k', label='identidade')

plt.legend()

#%% versão aula professor

def f(a,x):
    return a*x*(1-x)
a=2.9
t1 = np.arange(0.0, 1.0, 0.01)
x1_list=[]

for i in t1:
    y=f(a,i)
    x1_list.append(f(a,y))
t2 = np.arange(0.0, 1.0, 0.01)

plt.title('Close to cycle-1 bifurcation')
plt.plot(t1, x1_list, 'b', label='a=2.9')
plt.plot( t1,t2, 'k', label='identity')
plt.show()