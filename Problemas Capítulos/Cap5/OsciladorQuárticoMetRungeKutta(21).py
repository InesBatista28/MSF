import numpy as np
import matplotlib.pyplot as plt

# Parâmetros físicos
m = 1.0       # massa (kg)
k = 1.0       # constante elástica (N/m)
b = 0.05      # coef. de amortecimento (kg/s)
alpha = 1.0   # não-linearidade (N/m^2)
F0 = 7.5      # força externa (N)
omega = 1.0   # frequência forçada (rad/s)

# Tempo de simulação
dt = 0.001
T_max = 100
n = int(T_max / dt)
t = np.linspace(0, T_max, n)

# Condições iniciais (caso a)
x = np.zeros(n)
v = np.zeros(n)
x[0] = 3.0
v[0] = 0.0

# Lei do movimento (integração numérica - método de Euler)
for i in range(n - 1):
    F_spring = -k * x[i] * (1 + 2 * alpha * x[i]**2)
    F_damp = -b * v[i]
    F_ext = F0 * np.cos(omega * t[i])
    a = (F_spring + F_damp + F_ext) / m
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i+1] * dt

# Gráfico da posição vs tempo
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Oscilador Quártico Forçado - Lei do Movimento')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico no espaço de fase
plt.figure(figsize=(6, 6))
plt.plot(x, v)
plt.xlabel('Posição (m)')
plt.ylabel('Velocidade (m/s)')
plt.title('Espaço de Fase')
plt.grid(True)
plt.tight_layout()
plt.show()

# Energia mecânica total
def energia_mec(x, v):
    E_pot = 0.5 * k * x**2 * (1 + alpha * x**2)
    E_cin = 0.5 * m * v**2
    return E_pot + E_cin

E = energia_mec(x, v)

# Gráfico da energia mecânica
plt.figure(figsize=(10, 4))
plt.plot(t, E)
plt.xlabel('Tempo (s)')
plt.ylabel('Energia Mecânica (J)')
plt.title('Energia Mecânica ao Longo do Tempo')
plt.grid(True)
plt.tight_layout()
plt.show()
