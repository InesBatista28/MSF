import matplotlib.pyplot as plt
import numpy as np

g = 9.8
L = 0.5
theta0 = 0.1        # posição angular inicial (rad)
omega0 = 0.5        # velocidade angular inicial (rad/s)

t_max = 4 
dt = 0.01     
n = int(t_max / dt)

# Vetores de tempo, posição angular e velocidade angular
t = np.linspace(0, t_max, n)
theta = np.zeros(n)
omega = np.zeros(n)

# Condições iniciais
theta[0] = theta0
omega[0] = omega0

# Integração com método de Euler
for i in range(n - 1):
    alpha = -(g / L) * theta[i]  # aceleração angular
    omega[i+1] = omega[i] + alpha * dt
    theta[i+1] = theta[i] + omega[i+1] * dt

# a) Gráfico da posição angular ao longo do tempo
plt.figure(figsize=(10, 4))
plt.plot(t, theta)
plt.xlabel('Tempo (s)')
plt.ylabel('Ângulo (rad)')
plt.title('Lei do movimento do pêndulo simples (aproximação linear)')
plt.show()

# b) Cálculo da amplitude (máximo valor de theta)
amplitude = np.max(np.abs(theta))

# Encontrar picos (máximos locais) manualmente
indices_pico = []
for i in range(1, n-1):
    if theta[i-1] < theta[i] and theta[i] > theta[i+1]:
        indices_pico.append(i)

# Calcular o período com base nos dois primeiros picos
if len(indices_pico) >= 2:
    periodo = t[indices_pico[1]] - t[indices_pico[0]]
else:
    periodo = float('nan')

# Exibir os resultados
print(f"Amplitude aproximada: {amplitude:.4f} rad")
print(f"Período aproximado: {periodo:.4f} s")