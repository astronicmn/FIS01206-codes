#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
	DESCRIÇÃO:
      Integrando numericamente o Modelo de Epidemia SIR usando RK 3/8.
      Para simplificar a exploração do modelo use o parâmetro gamma = 0.5 
      e varie o parâmetro beta. 
      
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		
	VERSÃO:
	0.01 - 22/12/2022
    0.02 - 16/01/2023
    
"""
import numpy as np
import matplotlib.pyplot as plt

#%%
# beta --> taxa de infecção
# gamma --> taxa de remoção

def modeloSIR(x, deltaT, N, beta, gamma):
    S, I, R = x   # definindo S, I ,R como uma variável x 
    dS = -beta*S*I/N            
    dI = beta*S*I/N- gamma*I
    dR = gamma*I              
    
    return np.array([dS, dI, dR])

#%% Método Runge Kutta 3/8
    
def RK3_8(f, x0, deltaT, N, beta, gamma):
    x = x0
    listaX = [x0]
    h = deltaT[1]-deltaT[0] # h --> passo de integração
    
    for i in range(1, len(deltaT)):
        k1 = h * f(x, deltaT[i-1], N, beta, gamma)
        k2 = h * f(x + k1/3, deltaT[i-1] + h/3, N, beta, gamma)
        k3 = h * f(x + 2 * k2/3, deltaT[i-1] + 2 * h/3, N, beta, gamma)
        k4 = h * f(x + k3, deltaT[i], N, beta, gamma)
        x = x + (k1 + 3 * k2 + 3 * k3 + k4) / 8
        listaX.append(x)
        
    return np.array(listaX)

#%% 
def analiticoSIR(deltaT, N, beta, gamma, S0, I0, R0):
    S = S0 * np.exp(-beta*I0*deltaT/N)
    I = I0 * np.exp((beta*I0/N-gamma)*deltaT)
    R = R0 + N - S - I
    return S, I, R

S0 = 99
I0 = 1
R0 = 0
N = 100 #constante

listaBeta = [0.1, 0.4, 0.5, 0.6, 0.8] #variando parâmetro beta 
gamma = 0.5

x0 = np.array([S0, I0, R0])  #condições iniciais 
deltaT = np.linspace(0, 50, 1000)

#%% Suscetíveis para valores de beta
for beta in listaBeta:
    
    solucao = RK3_8 (modeloSIR, x0, deltaT, N, beta, gamma)
    S = solucao[:,0]
    plt.plot(deltaT, S, label='β = ' + str(beta))

plt.title('Suscetíveis')   
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()

#%% Infectados para valores de beta
for beta in listaBeta:
    
    solucao = RK3_8 (modeloSIR, x0, deltaT, N, beta, gamma)
    I = solucao[:,1]
    plt.plot(deltaT, I, label='β = ' + str(beta))

plt.title('Infectados')   
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()

#%% Removidos para valores de beta
for beta in listaBeta:
    
    solucao = RK3_8 (modeloSIR, x0, deltaT, N, beta, gamma)
    R = solucao[:,2]
    plt.plot(deltaT, R, label='β = ' + str(beta))

plt.title('Removidos')   
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()

#%% Analiticamente

for beta in listaBeta:
    analiticoS = S0 + (-beta*I0*S0*deltaT/N)
    analiticoI = I0 + ((beta*I0*S0*deltaT/N)-gamma*I0*deltaT)
    analiticoR = R0 + gamma*I0*deltaT
    
plt.plot(deltaT, analiticoS, label='S analítico', color = 'magenta')
plt.plot(deltaT, analiticoI, label='I analítico', color = 'red')
plt.plot(deltaT, analiticoR, label='R analítico', color = 'blue')
plt.xlabel('Tempo')
plt.ylabel('População')
plt.legend()
plt.show()