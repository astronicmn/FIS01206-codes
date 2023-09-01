#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    1) Partindo do valor inicial x = 0.7, faça um gráfico da evolução
    temporal do mapa logístico até 30 passos para os seguintes valores do 
    parâmetro a:
        - a = 0.1
        - a = 1.2
        - a = 3.1
        - a = 4
    Use pontos obtidos para fazer o gráfico, não use linhas para ligar os 
    pontos, pois essas não tem sentido físico.
    
    2) Use os mesmos parâmetros para fazer um gráfico de primeiro retorno do
    mapa logístico (x_n+1 X x_n).
    
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
	0.01 - 14/02/2023
"""
#%%
'''
import matplotlib.pyplot as plt

xn = 0.7
a = 0.1
n = 1
x0 = 0

passos = 30
contador = 0

listaX = [xn]
listaA = [a]

while contador < passos:
    xn1 = 0
    
    xn = a*xn*(1-xn)
    xn1 = a*xn*(1-xn1)
    
    xn1 = 1 - (1/a)
    
    listaX.append[xn]
    listaA.append[a]
    
plt.plot(listaX,listaA)
plt.show()
'''
#%%
import matplotlib.pyplot as plt

x = 0.7
n = 30

valoresA = [0.1, 1.2, 3.1, 4]

for a in valoresA:
    listaX = [x]
    
    for i in range(n):
        x = a * x * (1 - x)
        listaX.append(x)
        
    plt.plot(listaX, label=f"a={a}")
    plt.legend()
    
plt.xlabel("Número de iterações", )
plt.ylabel("Valor de x")
plt.title("Evolução temporal do mapa logístico para diferentes valores de a")
plt.show()