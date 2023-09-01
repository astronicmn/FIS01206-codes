#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	AULA 2
   
	DESCRIÇÃO:
		Aula 2 sobre Decaimento Radioativo utilizando Método de Euler
        Métodos de Euler IMPLÍCITO e EXPLÍCITO 

	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
		Teste de estabilidade do Método de Euler Explícito. 
        
        https://edisciplinas.usp.br/course/view.php?id=62404
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
	 
	VERSÃO:
	0.01 - 24/11/2022
"""
#%% Importando módulos

import numpy as np
import matplotlib.pyplot as plt

#%% Solução Analítica

x0 = 100
tau = 2
deltaT = 0.1 
t_final = 10.
t = 0
x = x0

xa_list = [100]
t_list = [0]

while t < t_final:
    t += deltaT
    t_list.append(t)
    xa_list.append(x0*np.exp(-t/tau))

plt.plot(t_list, xa_list, color='magenta')
plt.grid(True, linestyle='--')

#%% Integração Númerica Euler Explícito

deltaT_list = [0.1, 0.5, 1, 2]

for deltaT in deltaT_list:
    t = 0
    x = x0
    t_list = [t]
    x_list = [x]
    while t < t_final:
        x = x - x*deltaT/tau #integração numérica
        t = t + deltaT
        x_list.append(x)
        t_list.append(t)
    plt.plot(t_list, x_list, label = 'deltaT = ' + str(deltaT))
    
plt.legend()
plt.xlabel('Tempo')
plt.ylabel('X')
plt.grid(True, linestyle='--')

#%% Integração Numérica Euler Implícito

x0 = 100
tau = 2
deltaT = 0.1 
t_final = 10.
t = 0
x = x0

deltaT_list = [0.1, 0.5, 1, 2]

for deltaT in deltaT_list:
    t = 0
    x = x0
    t_list = [t]
    x_list = [x]
    while t < t_final:
        x = x/(1+(deltaT/tau)) #integração numérica
        t = t + deltaT
        x_list.append(x)
        t_list.append(t)
    plt.plot(t_list, x_list, label = 'deltaT = ' + str(deltaT))
    
plt.legend()
plt.xlabel('Tempo')
plt.ylabel('X')
plt.grid(True, linestyle='--')
plt.show()
