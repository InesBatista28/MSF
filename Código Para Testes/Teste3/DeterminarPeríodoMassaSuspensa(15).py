import numpy as np
import matplotlib.pyplot as plt

g = 9.8  
L = 1.0  
dt = 0.001
t_max = 20
n = int(t_max / dt)

angulos_graus = [5, 10, 20, 30]

def calcular_periodo(theta0_deg):
    theta0 = np.radians(theta0_deg)
    omega0 = 0.0

    t = np.linspace(0, t_max, n)
    theta = np.zeros(n)
    omega = np.zeros(n)

    # Condições iniciais
    theta[0] = theta0
    omega[0] = omega0

    # Método de Euler
    for i in range(n - 1):
        alpha = - (g / L) * np.sin(theta[i])
        omega[i + 1] = omega[i] + alpha * dt
        theta[i + 1] = theta[i] + omega[i + 1] * dt

    # Detectar picos (máximos locais) 
    indices_pico = []
    for i in range(1, n - 1):
        if theta[i - 1] < theta[i] and theta[i] > theta[i + 1]:
            # só consideramos picos após o tempo t=0.5s para evitar o ponto inicial
            if t[i] > 0.5:
                indices_pico.append(i)

    if len(indices_pico) >= 2:
        periodo = t[indices_pico[1]] - t[indices_pico[0]]
    else:
        periodo = float('nan')

    return periodo

# Calcular períodos
for ang in angulos_graus:
    T = calcular_periodo(ang)
    if np.isnan(T):
        print(f"Ângulo inicial: {ang:>2}° → Não foram detectados dois picos.")
    else:
        print(f"Ângulo inicial: {ang:>2}° → Período ≈ {T:.3f} s")
