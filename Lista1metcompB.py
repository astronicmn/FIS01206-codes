#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    DESCRIÇÃO: Lista 1 de Problemas Métodos Computacionais B.

	AUTOR:
		N. M. Narvaz 
		00318736@ufrgs.br
	
	REFERÊNCIAS: 
		<[#] referência..>
	
	BUGS/LIMITAÇÕES:

	ToDos:
		<alterações/correções a fazer>
	
	OBSERVAÇÕES:
		Para tornar executável:
		% chmod ugo+x <nome_do_programa>
		
		Para criar um link em ~/bin:
		% ln ~/prog/python/programa.py> ~/bin/<programa>
	 
	VERSÃO:
	0.01 - 08/02/2023
"""

#%% 
# 1. No problema do decaimento radioativo, dx/dt = − α x ; x(0) = x0 , determine o limite superior 
# do passo de tempo ∆t para o qual o método de Euler converge para uma solução assintótica nula.

#--------------------------------------------------------------------------------------------------
# A equação diferencial que descreve o decaimento radioativo é dada por dx/dt = -αx, onde x é 
# a quantidade de material radioativo presente em um determinado momento e α é uma constante 
# de taxa de decaimento.
# O método de Euler é um método de integração numérica que pode ser usado para aproximar
#  soluções de equações diferenciais. Ele é baseado na ideia de calcular a variação da
#  quantidade x ao longo do tempo com base na equação diferencial e no valor de x em um
#  momento anterior. O passo de tempo ∆t é a diferença de tempo entre duas iterações 
# consecutivas do método de Euler.
#Para garantir que o método de Euler converge para uma solução assintótica nula, o
#  passo de tempo ∆t precisa ser suficientemente pequeno. O limite superior desse passo de tempo 
# é dado por:
# ∆t < 2 / α
# Isso significa que, para garantir a convergência, o passo de tempo ∆t não pode 
# ser maior que 2 / α. Este é o limite máximo para o qual o método de Euler é 
# garantido para convergir para uma solução assintótica nula.

import numpy as np
import matplotlib.pyplot as plt

def decay(x, alpha):
    return -alpha * x

alpha = 0.05
x0 = 100
t0 = 0
tf = 10
delta_t = 0.01

t = np.arange(t0, tf, delta_t)
x = np.zeros_like(t)
x[0] = x0

for i in range(1, len(t)):
    x[i] = x[i-1] + delta_t * decay(x[i-1], alpha)

plt.plot(t, x)
plt.xlabel('Tempo (t)')
plt.ylabel('Quantidade de material radioativo (x)')
plt.show()

#%%
# 2. No problema do decaimento radioativo, dx/dt = − α x ; x(0) = x0 ,
# determine o limite superior do passo de tempo ∆t para o qual
# o método do Ponto Médio (Runge-Kutta em segunda ordem)
# converge para uma solução assintótica nula.

#---------------------------------------------------------------------------------

# O método do Ponto Médio, também conhecido como o método de Runge-Kutta de segunda ordem, 
# é um método numérico para aproximar a solução de uma equação diferencial. Para o problema 
# do decaimento radioativo, ele pode ser escrito como:

# x(t + ∆t) = x(t) + (∆t/2) * (f(t, x(t)) + f(t + ∆t, x(t) + ∆t * f(t, x(t))))
# onde f(t, x) = -α * x.

# Para determinar o limite superior do passo de tempo ∆t, precisamos avaliar a condição de 
# estabilidade para o método. Uma condição comum para a estabilidade é que o passo de tempo
# ∆t deve ser suficientemente pequeno para que a solução não diverja para valores inapropriados.
#  Em geral, isso significa que a magnitude da taxa de mudança de x(t) em relação a t deve ser
#  suficientemente pequena para que a solução seja controlável.
# No caso do decaimento radioativo, a taxa de mudança é dada por f(t, x) = -α * x, ou seja, 
# é negativa e proporcional à magnitude de x. Portanto, quanto menor for o valor de x, menor 
# será a taxa de mudança. Isso sugere que quanto mais perto de zero for x(t), menor será o
#  passo de tempo que pode ser usado sem correr o risco de divergência.
# 
# Ainda assim, a condição exata para o limite superior do passo de tempo ∆t depende da taxa 
# de decaimento α e do erro tolerado na solução. Infelizmente, não é possível determinar um 
# valor exato sem mais informações específicas sobre o problema em questão. No entanto, em geral,
# o valor de ∆t pode ser ajustado iterativamente até que a solução satisfaça as condições desejadas.

import numpy as np
import matplotlib.pyplot as plt

def decay_radioactive(alpha, x0, t, dt):
    t_vals = np.arange(0, t, dt)
    x = np.zeros_like(t_vals)
    x[0] = x0

    for i in range(1, len(t_vals)):
        x[i] = x[i-1] + (dt/2) * (-alpha * x[i-1] + -alpha * (x[i-1] + dt * -alpha * x[i-1]))

    return t_vals, x

alpha = 0.1
x0 = 100
t = 10
dts = [0.1, 0.01, 0.001]

for dt in dts:
    t_vals, x = decay_radioactive(alpha, x0, t, dt)
    plt.plot(t_vals, x, label=f"dt={dt}")

plt.xlabel("Time (t)")
plt.ylabel("x(t)")
plt.legend()
plt.show()



#%%
# 3. No problema do decaimento radioativo,dx dt = − α x ; x(0) = x0 ,
#  determine o limite superior do passo de tempo ∆t para o qual o método
#  de Heun converge para uma solução assintótica nula. O método de Heun usa 
# a média entre as derivadas no início e final do intervalo ∆t:
#  x(t + ∆t) = x(t) + ∆t × (1) {f(t, x(t)) + f[t + ∆t, x(t) + ∆tf(t, x(t))]}/2. (2)

# -------------------------------------------------------------------------------------

# Infelizmente, não há uma fórmula exata para determinar o limite superior do passo de tempo 
# ∆t para o qual o método de Heun converge para uma solução assintótica nula. Isso depende do
# valor específico de α e da precisão desejada para a solução.No entanto, em geral, quanto menor
#  o passo de tempo ∆t, mais precisa será a solução. Para garantir a convergência, é geralmente
#  necessário escolher um passo de tempo ∆t suficientemente pequeno, o que pode ser determinado 
# por experimentação ou por um critério de estabilidade numérica.Aqui está um exemplo de como 
# você pode implementar o método de Heun para resolver a equação diferencial do decaimento 
# radioativo:

import numpy as np
import matplotlib.pyplot as plt

def decay(x, t, alpha):
    return -alpha * x

def heun(x0, t0, tf, alpha, delta_t):
    t = np.arange(t0, tf, delta_t)
    x = np.zeros_like(t)
    x[0] = x0
    
    for i in range(1, len(t)):
        x_mid = x[i-1] + delta_t/2 * decay(x[i-1], t[i-1], alpha)
        x[i] = x[i-1] + delta_t * decay(x_mid, t[i-1] + delta_t/2, alpha)
        
    return t, x

alpha = 0.05
x0 = 100
t0 = 0
tf = 10
delta_t = 0.01

t, x = heun(x0, t0, tf, alpha, delta_t)

plt.plot(t, x)
plt.xlabel('Tempo (t)')
plt.ylabel('Quantidade de material radioativo (x)')
plt.show()


#%%
# 4. No problema do decaimento radioativo, dx dt = − α x ; x(0) = x0 ,
#  determine o limite superior do passo de tempo ∆t para o qual o método 
# de Ralston converge para uma solução assintótica nula. O método de Ralston 
# usa uma média ponderada entre as derivadas no início e final do intervalo
# ∆t: x(t + ∆t) = x(t) + ∆t{f(t, x(t)) + (3) 2f[t + 3 4 ∆t, x(t) + 3 4 ∆tf(t, x(t))]}/3. (4)

#----------------------------------------------------------------------------------------------

#O método de Ralston é uma técnica numérica de integração de equações diferenciais. Para determinar 
# o limite superior do passo de tempo ∆t para o qual o método de Ralston converge para uma solução 
# assintótica nula, é necessário realizar análise de estabilidade. A análise de estabilidade
# verifica se a solução numérica converge para a solução exata conforme ∆t se torna menor. 
# Em geral, quanto menor o passo de tempo, mais precisa é a solução numérica. No entanto, 
# também é importante verificar se o método é estável, ou seja, se pequenas perturbações na solução 
# não se amplificam ao longo do tempo. No caso do método de Ralston, a estabilidade é garantida se o
#  passo de tempo ∆t satisfaz a seguinte condição:
#  ∆t < 2/α
# Portanto, o limite superior do passo de tempo para o qual o método de Ralston converge para 
# uma solução assintótica nula é de 2/α.
# Este código resolve a equação diferencial usando o método de Euler explícito. 
# O valor inicial de x é armazenado na variável x0, e o tempo final é especificado 
# por t_final. O passo de tempo é definido por dt, e o tempo é discretizado usando 
# o np.arange da biblioteca numpy. Em seguida, a solução é atualizada usando o método de 
# Euler explícito em um loop for, armazenando os valores resultantes em um vetor x. Finalmente, 
# a solução é plotada usando a biblioteca matplotlib.

import numpy as np
import matplotlib.pyplot as plt

α = 1
x0 = 1
t_final = 10
dt = 0.01

def fun(x, t):
    return -α * x

t = np.arange(0, t_final, dt)
x = np.zeros(len(t))
x[0] = x0

for i in range(1, len(t)):
    x[i] = x[i-1] + dt * fun(x[i-1], t[i-1])

plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()



#%%
# 5. Mostre que o método de Runge Kutta 4 descrito por 
# K1 = hf(t, xn) 
# K2 = hf(t + h 2 , xn + K1 2 ) 
# K3 = hf(t + h 2 , xn + K2 2 ) 
# K4 = hf(t + h, xn + K3) xn+1 = xn + 1 6 (K1 + 2K2 + 2K3 + K4) 
# Quando aplicado a uma equação diferencial dx dt = λxn ,pode ser reescrita como:
# xn+1 = (1 + hλ + 1 2 (hλ) 2 + 1 6 (hλ) 3 + 1 24 (hλ) 4 )xn de modo a 
# demonstrar o método como expansão da série de taylor até a ordem de erro O(h 4 ).

#------------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def f(t, x):
    return -lambda_value*x

def runge_kutta_4(t0, x0, h, lambda_value):
    k1 = h*f(t0, x0)
    k2 = h*f(t0 + h/2, x0 + k1/2)
    k3 = h*f(t0 + h/2, x0 + k2/2)
    k4 = h*f(t0 + h, x0 + k3)
    
    x1 = x0 + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    return x1

lambda_value = 2
h = 0.01
t0 = 0
x0 = 1
T = 5
N = int(T/h)

x = np.zeros(N)
t = np.zeros(N)

x[0] = x0
t[0] = t0

for i in range(1, N):
    x[i] = runge_kutta_4(t[i-1], x[i-1], h, lambda_value)
    t[i] = t[i-1] + h

plt.plot(t, x, '-o')
plt.xlabel('t')
plt.ylabel('x')
plt.show()



#%%
#6. Usando o método de Adams-Bashforth xn+1 = xn + 3 2 ∆t f(xn) − 1 2 ∆t f(xn−1) 
# e Adams-Moulton xn+1 = xn + 1 2 ∆t f(xn+1) + 1 2 ∆t f(xn) a) Escreva um algoritmo 
# do tipo predição-correção para o problema do sistema abaixo d 2x dt2 = −k x. b)
#  Na linguagem que lhe for familiar, escreva o programa correspondente. 
# c) Com base na solução analítica, faça uma estimativa para um valor inicial de ∆t. 
# Justifique a sua resposta.

#-------------------------------------------------------------------------------------

# a) Algoritmo de predição-correção:
# Inicialize as variáveis t, x e v (velocidade inicial). Calcule o primeiro passo usando um 
# método numérico inicial, como o método de Euler. Armazene o valor de xn−1. A partir de xn, 
# calcule o próximo passo xn+1 usando o método de Adams-Bashforth:
#  xn+1 = xn + 3/2 * ∆t * f(xn) - 1/2 * ∆t * f(xn−1) Atualize xn para xn+1. 
# Calcule xn+1 novamente usando o método de Adams-Moulton: 
# xn+1 = xn + 1/2 * ∆t * f(xn+1) + 1/2 * ∆t * f(xn) Atualize xn para xn+1. 
# Repita os passos 4-7 até que t atinja o tempo final desejado.
# c) A estimativa para o valor inicial de Δt pode ser feita com base na solução analítica 
# do problema. A solução analítica para a equação diferencial acima é dada por
# x(t) = A cos(√k t) + B sen(√k t)
# onde A e B são constantes que dependem das condições iniciais.
#  A partir daqui, podemos calcular a freqüência natural do sistema, que é dada por √k,
#  e usá-la para estimar um valor inicial para Δt. Por exemplo, se Δt for muito grande, 
# as soluções numéricas podem ficar instáveis. Se Δt for muito pequeno, o cálculo pode
#  levar muito tempo. Portanto, uma boa prática é escolher Δt de tal forma que o número 
# de oscilações seja de pelo menos 10 a 20 dentro do intervalo de tempo desejado. 
# Isso pode ser feito usando a equação:
# Δt = 2π / (10 a 20 x √k)
# onde Δt é o passo de tempo desejado.

import numpy as np

def adams_bashforth_moulton(x0, v0, k, T, dt):
    # Define o número de passos
    N = int(T / dt)
    # Inicializa as listas de tempo e soluções
    t = np.linspace(0, T, N+1)
    x = np.zeros(N+1)
    v = np.zeros(N+1)
    x[0] = x0
    v[0] = v0
    # Define o primeiro passo usando o método de Euler
    x[1] = x[0] + v[0] * dt
    v[1] = v[0] - k * x[0] * dt
    # Loop do método predição-correção
    for i in range(1, N):
        # Predição usando o método de Adams-Bashforth
        x_pred = x[i] + 3/2 * dt * v[i] - 1/2 * dt * v[i-1]
        v_pred = v[i] - k * x[i] * dt
        # Correção usando o método de Adams-Moulton
        x[i+1] = x[i] + 1/2 * dt * (v[i] + v_pred)
        v[i+1] = v[i] - 1/2 * dt * (k * x[i+1] + k * x[i])
    return t, x, v

#%%
#7. Dada a tabela de Butcher, 
# 0 0 0 0 1/2 1/2 0 0 1 -1 2 0 1/6 2/3 1/6 escreva o algoritmo Runge-Kuta correspondente.

#-----------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def f(t, x):
    return -x

def runge_kutta_4(f, t0, x0, h, n):
    t = t0
    x = x0
    times = [t0]
    xs = [x0]
    for i in range(n):
        k1 = h * f(t, x)
        k2 = h * f(t + h/2, x + k1/2)
        k3 = h * f(t + h/2, x + k2/2)
        k4 = h * f(t + h, x + k3)
        x = x + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        times.append(t)
        xs.append(x)
    return times, xs

t0 = 0
x0 = 1
h = 0.1
n = 10
times, xs = runge_kutta_4(f, t0, x0, h, n)

plt.plot(times, xs)
plt.xlabel("Time")
plt.ylabel("x")
plt.title("Runge-Kutta Solution")
plt.show()

#%%
# 8. Descreva um algoritmo para encontrar numericamente a ordem do erro 
# global de um método de integração numérico qualquer. 
# Explique como deve ser feito o ajuste para que se encontre a lei de potência associada.

# -----------------------------------------------------------------------------------------

# O algoritmo para encontrar a ordem do erro global de um método de integração numérico é baseado na análise 
# da diferença entre a solução numérica e a solução exata em função do tamanho do passo de tempo ∆t. O procedimento é o seguinte:
# Escolha uma equação diferencial com solução conhecida, geralmente uma equação com solução analítica simples.
# Escolha um valor inicial de ∆t e resolva a equação diferencial usando o método de integração numérico escolhido.
# Calcule a solução exata para o mesmo período de tempo usando a solução analítica.
# Calcule a diferença absoluta entre as soluções numéricas e exatas em vários pontos.
# Repita os passos 2 a 4 para diferentes valores de ∆t, mantendo a proporção entre eles (por exemplo, ∆t/2, ∆t/4, ∆t/8).
# Plotar a diferença absoluta entre as soluções numéricas e exatas em função de ∆t e calcular a inclinação da reta resultante.
# Repita os passos 2 a 6 para várias equações diferenciais diferentes.
# O resultado da inclinação da reta resultante fornecerá a ordem do erro global do método de integração numérico. 
# Para encontrar a lei de potência associada, é necessário ajustar a equação da reta resultante para a forma y = C∆t^p,
# onde C é uma constante e p é a ordem do erro global.



#%%
# 9. Na aproximação de ângulos pequenos, a energia total de um pêndulo simples é E = 1 2 mL2ω 2 + 1 2 mgLθ2 .
# Mostre analiticamente que E aumenta monotonicamente com o tempo quando o método de Euler é utilizado na integração numérica. 
# O que acontece quando utilizamos o método de EulerCromer? 

#---------------------------------------------------------------------------------------------------

# A energia total de um pêndulo simples é dada por:
# E = 1/2 * mL^2 * ω^2 + 1/2 * m * g * L * θ^2
# Onde mL^2 * ω^2 é a energia cinética e 1/2 * m * g * L * θ^2 é a energia potencial devido à posição angular θ do pêndulo.
# Quando o método de Euler é utilizado na integração numérica, ele é uma aproximação iterativa da solução. No entanto, 
# ele pode levar a uma acumulação de erro ao longo do tempo, resultando em um aumento na energia total.
# Por outro lado, o método de Euler-Cromer é uma variação do método de Euler que utiliza uma atualização diferente para 
# a velocidade. Ele corrige o erro do método de Euler e, como resultado, preserva a energia total de forma mais exata. 
# Portanto, a energia total não aumenta monotonicamente com o tempo quando o método de Euler-Cromer é utilizado.

import numpy as np
import matplotlib.pyplot as plt

def pendulo_euler(theta0, omega0, t, L, m, g):
    # Calcula as soluções usando o método de Euler
    N = t.shape[0]
    theta = np.zeros(N)
    omega = np.zeros(N)
    theta[0] = theta0
    omega[0] = omega0
    dt = t[1] - t[0]
    for i in range(1, N):
        omega[i] = omega[i-1] - (g/L) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i] * dt
    return theta, omega

def pendulo_euler_cromer(theta0, omega0, t, L, m, g):
    # Calcula as soluções usando o método de Euler-Cromer
    N = t.shape[0]
    theta = np.zeros(N)
    omega = np.zeros(N)
    theta[0] = theta0
    omega[0] = omega0
    dt = t[1] - t[0]
    for i in range(1, N):
        omega[i] = omega[i-1] - (g/L) * np.sin(theta[i-1]) * dt
        theta[i] = theta[i-1] + omega[i] * dt
        omega[i] = omega[i] - (g/L) * np.sin(theta[i]) * dt
    return theta, omega

# Define os parâmetros do problema
L = 1
m = 1
g = 9.8
t = np.linspace(0, 10, 1000)
theta0 = 0.1
omega0 = 0

# Calcula as soluções usando os métodos de Euler e Euler-Cromer
theta_euler, omega_euler = pendulo_euler(theta0, omega0, t, L, m, g)
theta_ec, omega_ec = pendulo_euler_cromer(theta0, omega0, t, L, m, g)

# Plota as soluções
plt.plot(t, theta_euler, label="Euler")
plt.plot(t, theta_ec, label="Euler-Cromer")
plt.xlabel("Tempo (s)")
plt.ylabel("Ángulo (rad)")
plt.legend()
plt.show()


#%%
# 10. Prove que para o problema de Kepler o método de EulerCromer conserva momentum angular de forma exata.
# O que ocorre quando se utiliza o método de Euler?

#----------------------------------------------------------------------------------------------------------

# O método de Euler-Cromer é um método numérico para resolver equações diferenciais ordinárias. 
# É uma variação do método de Euler, que utiliza uma correção para evitar o erro acumulativo.
# No problema de Kepler, a equação da dinâmica é dada por:
# x''(t) = -(GM/r^3) x(t) y''(t) = -(GM/r^3) y(t)
# onde r = √(x^2 + y^2), e GM é a constante gravitacional.
#  O momento angular é dado por L = x * y' - y * x'.
# Com o método de Euler-Cromer, as atualizações da posição e da velocidade são dadas por:
# x(t + Δt) = x(t) + Δt * vx(t + Δt/2) 
# y(t + Δt) = y(t) + Δt * vy(t + Δt/2) 
# vx(t + Δt) = vx(t) + Δt * -(GM/r^3) x(t + Δt) 
# vy(t + Δt) = vy(t) + Δt * -(GM/r^3) y(t + Δt)
# Com estas atualizações, o momento angular é conservado,
#  ou seja, L(t + Δt) = L(t), 
# pois x(t + Δt) * vy(t + Δt) - y(t + Δt) * vx(t + Δt) = x(t) * vy(t) - y(t) * vx(t). 
# Isto significa que o método de Euler-Cromer conserva o momento angular de forma exata.
# No entanto, quando o método de Euler é utilizado, as atualizações da posição e da velocidade
#  são dadas por:
# x(t + Δt) = x(t) + Δt * vx(t) 
# y(t + Δt) = y(t) + Δt * vy(t) 
# vx(t + Δt) = vx(t) + Δt * -(GM/r^3) x(t) 
# vy(t + Δt) = vy(t) + Δt * -(GM/r^3) y(t)
# Com estas atualizações, o momento angular não é conservado, ou seja, 
# L(t + Δt) ≠ L(t), 
# pois x(t + Δt) * vy(t + Δt) - y(t + Δt) * vx(t + Δt) ≠ x(t) * vy(t) - y(t) * vx(t). 
# Portanto, o método de Euler não conserva o momento angular de forma exata.




#%%
#11. Integre numericamente a equação associada à dinâmica de
# um cometa na vizinhança do Sol. Use método de passo variável com RK2 corrigido
# por RK4. 
# Use GM=1. Condições iniciais: 
# • x=0; y=4; vx=-1/2; vy=0 (órbita circular) 
# • x=0; y=4; vx=-1/4; vy=0 (órbita elíptica 1) 
# • x=0; y=4; vx=-0.65; vy=0 (órbita elíptica 2) 
# • x=0; y=4; vx=-sqrt(2)/2; vy=0 (órbita parabólica)
#  • x=0; y=4; vx= -1; vy=0 (órbita hiperbólica)

#--------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def rk2_rk4(f, t, x, h):
    k1 = h * f(t, x)
    k2 = h * f(t + h / 2, x + k1 / 2)
    k3 = h * f(t + h / 2, x + k2 / 2)
    k4 = h * f(t + h, x + k3)
    return x + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def comet_dynamics(t, x):
    r = np.sqrt(x[0]**2 + x[1]**2)
    return np.array([x[2], x[3], -x[0] / r**3, -x[1] / r**3])

x0 = [0, 4, -0.5, 0]  # Orbita circular
x0 = [0, 4, -0.25, 0]  # Orbita elíptica 1
x0 = [0, 4, -0.65, 0]  # Orbita elíptica 2
x0 = [0, 4, -np.sqrt(2)/2, 0]  # Orbita parabólica
x0 = [0, 4, -1, 0]  # Orbita hiperbólica

t0 = 0
tf = 10
h = 0.01

x = np.array(x0)
t = t0

t_array = []
x_array = []
y_array = []

while t <= tf:
    t_array.append(t)
    x_array.append(x[0])
    y_array.append(x[1])
    x = rk2_rk4(comet_dynamics, t, x, h)
    t = t + h

plt.plot(x_array, y_array)
plt.xlabel("x")
plt.ylabel("y")
plt.show()