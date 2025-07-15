import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
k = 1.0       # N/m
k_p = 0.5     # N/m
m = 1.0       # kg
b = 0.05      # kg/s (amortecimento)
F = 0.005     # N (força externa)
xA_eq = 1.0   # m
xB_eq = 1.2   # m

# Parâmetros da simulação
dt = 0.01
T_total = 150.0
N = int(T_total / dt)
t = np.linspace(0, T_total, N)

# Função para simular o movimento para um dado omega
def simulate_motion(omega):
    xA = np.zeros(N)
    vA = np.zeros(N)
    xB = np.zeros(N)
    vB = np.zeros(N)

    # Condições iniciais
    xA[0] = xA_eq + 0.05
    vA[0] = 0
    xB[0] = xB_eq + 0.05
    vB[0] = 0

    for i in range(N - 1):
        # Forças
        FA = (-k * (xA[i] - xA_eq)
              - k_p * ((xA[i] - xA_eq) - (xB[i] - xB_eq))
              - b * vA[i]
              + F * np.cos(omega * t[i]))

        FB = (-k * (xB[i] - xB_eq)
              - k_p * ((xB[i] - xB_eq) - (xA[i] - xA_eq))
              - b * vB[i])

        # Acelerações
        aA = FA / m
        aB = FB / m

        # Euler para velocidade e posição
        vA[i+1] = vA[i] + aA * dt
        xA[i+1] = xA[i] + vA[i+1] * dt

        vB[i+1] = vB[i] + aB * dt
        xB[i+1] = xB[i] + vB[i+1] * dt

    return t, xA, xB

# --- Parte (a) ---
omega_a = 1.0  # rad/s
t_a, xA_a, xB_a = simulate_motion(omega_a)

plt.figure(figsize=(12,6))
plt.plot(t_a, xA_a, label='Corpo A')
plt.plot(t_a, xB_a, label='Corpo B')
plt.title('Posições dos corpos (ω=1 rad/s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.legend()
plt.grid(True)
plt.show()


# --- Parte (b) ---
# Frequências omega de 0 a 2.5 rad/s
omegas = np.linspace(0, 2.5, 50)
amplitudes_A = []
amplitudes_B = []

for w in omegas:
    t_tmp, xA_tmp, xB_tmp = simulate_motion(w)
    
    # Regime estacionário: usar últimos 20% do sinal para medir amplitude
    start_index = int(0.8 * N)
    xA_ss = xA_tmp[start_index:] - xA_eq
    xB_ss = xB_tmp[start_index:] - xB_eq
    
    amp_A = (np.max(xA_ss) - np.min(xA_ss)) / 2
    amp_B = (np.max(xB_ss) - np.min(xB_ss)) / 2
    
    amplitudes_A.append(amp_A)
    amplitudes_B.append(amp_B)

plt.figure(figsize=(12,6))
plt.plot(omegas, amplitudes_A, label='Amplitude Corpo A')
plt.plot(omegas, amplitudes_B, label='Amplitude Corpo B')
plt.title('Amplitude de oscilação em função de ω')
plt.xlabel('ω (rad/s)')
plt.ylabel('Amplitude (m)')
plt.legend()
plt.grid(True)
plt.show()
