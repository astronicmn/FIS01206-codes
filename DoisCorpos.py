#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	DESCRIÇÃO: Problema de dois corpos sob atração gravitacional.
    
    Integre numericamente a equação associada à dinâmica de um cometa na 
    vizinhança do Sol. Use método de passo variável com RK2 corrigido por RK4.
    Use GM=1.

    Condições iniciais:

    1. x=0; y=4; vx=-1/2; vy=0 (órbita circular)
    2. x=0; y=4; vx=-1/4; vy=0 (órbita elíptica 1)
    3. x=0; y=4; vx=-0.65; vy=0 (órbita elíptica 2)
    4. x=0; y=4; vx=-sqrt(2)/2; vy=0 (órbita parabólica)
    5. x=0; y=4; vx= -1; vy=0 (órbita hiperbólica)
  
	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
    moodle.ufrgs.br/pluginfile.php/5640539/mod_resource/content/2
    /problema-dois-corpos.pdf
    
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		
	VERSÃO:
	0.01 - 26/01/2023

"""
#%%
import numpy as np
import matplotlib.pyplot as plt

# órbita circular
x = 0
y = 4
vx = -1/2
vy = 0

def fx(v):
  return v

def fv(t,x):
  return 

def RK2(x, v, deltaT, t):
    
    k1x = fx(v)
    k1v = fv(t, x)
  
    xaux = x + k1x * (deltaT/2)
    vaux = v + k1v * (deltaT/2)
  
    k2x = fx(vaux)
    k2v = fv(t, xaux)
  
    x = x + k2x * deltaT
    v = v + k2v * deltaT
    
    return x, v

def RK4(x, v, deltaT, t):
    
    k1x = fx(v)
    k1v = fv(t,x)
  
    xaux = x + k1x * (deltaT/2)
    vaux = v + k1v * (deltaT/2)
    k2x = fx(vaux)
    k2v = fv(t + (deltaT/2), xaux)
  
    x = x + k2x * deltaT
    v = v + k2v * deltaT
  
    xaux = x + k2x * (deltaT/2)
    vaux = v + k2v * (deltaT/2)
    k3x = fx(vaux)
    k3v = fv(t + (deltaT/2), xaux)
  
    xaux = x + k3x * (deltaT)
    vaux = v + k3v * (deltaT)
    k4x = fx(vaux)
    k4v = fv(t + deltaT, xaux)
  
    x = x + (deltaT/6)*(k1x + 2*k2x + 2*k3x + k4x)
    v = v + (deltaT/6)*(k1v + 2*k2v + 2*k3v + k4v)
    t += deltaT
    
    return x, v



















