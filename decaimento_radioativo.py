#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
   
	DESCRIÇÃO:
		Utilizando algoritmo Método de Euler para Decaimento Radioativo
        dx/dt = -x/tau ; x(t=0) = x0

	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
		https://edisciplinas.usp.br/course/view.php?id=62404
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
	
	VERSÃO:
	0.01 - 22/11/2022
"""

#%% Importando módulos:

import matplotlib.pyplot as plt
import numpy as np

#%% 

def f(x, tau):
    return -x/tau

x0 = 100
x = x0
tau = 2
t = 0
t_final = 10
delta_t = 0.1

x_list = [x]
xa_list = [x]
t_list = [0]

while t < t_final:
    x = x + f(x, tau) * delta_t
    t = t + delta_t
    x_list.append(x)
    t_list.append(t)
    xa_list.append(x0*np.exp(-t/tau))
    
plt.plot(t_list, x_list,  label = 'x --> Numérico')
plt.plot(t_list, xa_list, label = 'xa --> Analítico')

plt.legend(loc = 0)
plt.grid(True, linestyle='--')
plt.show()
