#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    MÉTODOS MULTI PASSOS - Oscilador de van der Pool
    
      Integre numericamente o OvdP usando método multipasso
      explícito com s=1. Use x(0) = 0.5 e v(0) = 0
        
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		
	VERSÃO:
	0.01 - 31/01/2023
    0.02 - 08/02/2023

"""
#%% Através de gráficos X x T, V x T e X x V, mostre que o OvdP se reduz ao
#   OHS no limite mi = 0.

import matplotlib.pyplot as plt

v0 = 0
v = v0

x0 = 0.5
x = x0

tf, t = 20, 0
t1 = 0

deltaT = 0.1
mi = 0

x_list = [x0]
v_list = [v0]
t_list = [0]

def fv(t, x0, v0, mi):
    return mi*(1 - (v0**2))*v0 - x0

def fx(v):
    return v

while t < tf:
    
    x2 = x + deltaT*((3/2)*fx(v)-(1/2)*fx(v0))
    
    v2 = v + deltaT*((3/2)*fv(t1,x,v,mi)-(1/2)*fv(t,x0,v0,mi))
    
    x0 = x2
    x = x2
    
    v0 = v
    v = v2
    
    t1 += deltaT
    t += deltaT
    
    x_list.append(x2)
    v_list.append(v2)
    t_list.append(t)

#%% GRÁFICO X x T
plt.plot(t_list, x_list, color = 'purple')
plt.title('GRÁFICO X x T')

#%% GRÁFICO V x T
plt.plot(t_list, v_list, color = 'magenta')
plt.title('GRÁFICO V x T')

#%% GRÁFICO X x V
plt.plot(x_list, v_list, color = 'cyan')
plt.title('GRÁFICO X x V')

#%% 
#### Gráficos X x T e V x T para MI = 0.5

v0 = 0
v = v0

x0 = 0.5
x = x0

tf, t = 20, 0
t1 = 0

deltaT = 0.1
mi = 0.5

x_list = [x0]
v_list = [v0]
t_list = [0]

def fv(t, x0, v0, mi):
    return mi*(1 - (v0**2))*v0 - x0

def fx(v):
    return v

while t < tf:
    
    x2 = x + deltaT*((3/2)*fx(v)-(1/2)*fx(v0))
    
    v2 = v + deltaT*((3/2)*fv(t1,x,v,mi)-(1/2)*fv(t,x0,v0,mi))
    
    x0 = x2
    x = x2
    
    v0 = v
    v = v2
    
    t1 += deltaT
    t += deltaT
    
    x_list.append(x2)
    v_list.append(v2)
    t_list.append(t)

# GRÁFICO X x T
plt.plot(t_list, x_list, color = 'purple', label = 'X x T')

#  GRÁFICO V x T
plt.plot(t_list, v_list, color = 'magenta', label = 'V x T')

plt.legend(loc = 10)

#%% 
####  Gráficos X x T e V x T para MI = 4.0
v0 = 0
v = v0

x0 = 0.5
x = x0

tf, t = 20, 0
t1 = 0

deltaT = 0.1
mi = 4.0

x_list = [x0]
v_list = [v0]
t_list = [0]

def fv(t, x0, v0, mi):
    return mi*(1 - (v0**2))*v0 - x0

def fx(v):
    return v

while t < tf:
    
    x2 = x + deltaT*((3/2)*fx(v)-(1/2)*fx(v0))
    
    v2 = v + deltaT*((3/2)*fv(t1,x,v,mi)-(1/2)*fv(t,x0,v0,mi))
    
    x0 = x2
    x = x2
    
    v0 = v
    v = v2
    
    t1 += deltaT
    t += deltaT
    
    x_list.append(x2)
    v_list.append(v2)
    t_list.append(t)

# GRÁFICO X x T
plt.plot(t_list, x_list, color = 'purple', label = 'X x T')

#  GRÁFICO V x T
plt.plot(t_list, v_list, color = 'magenta', label = 'V x T')

plt.legend(loc = 10)

