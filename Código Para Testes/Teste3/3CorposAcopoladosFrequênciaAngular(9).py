import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
k = 1.0
k_p = 0.5
m = 1.0

# Matriz de constantes elásticas K
K = np.array([
    [k + k_p, -k_p,      0],
    [-k_p,    2*k_p,    -k_p],
    [0,       -k_p,  k + k_p]
])

# (a) Cálculo de valores próprios e vetores próprios
vals, vecs = np.linalg.eigh(K)  # eigh para matriz simétrica

# Frequências angulares
omega = np.sqrt(vals)

print("Frequências angulares (rad/s):")
for i, w in enumerate(omega):
    print(f"Modo {i+1}: ω = {w:.4f}")

# (b) Simulação pelo método de Euler-Cromer para cada modo normal

# Parâmetros de simulação
dt = 0.01
T = 20
N = int(T/dt)
t = np.linspace(0, T, N)

def euler_cromer_mode(omega_mode, mode_shape):
    # Inicializar arrays
    u = np.zeros((3, N))  # posições: A, B, C
    v = np.zeros((3, N))  # velocidades

    # Condição inicial: deslocamento proporcional ao modo normal, velocidade zero
    u[:, 0] = mode_shape / np.linalg.norm(mode_shape)  # normaliza o modo

    for i in range(N-1):
        a = -omega_mode**2 * u[:, i]  # aceleração harmônica para o modo
        v[:, i+1] = v[:, i] + a * dt
        u[:, i+1] = u[:, i] + v[:, i+1] * dt

    return u

# Plotando os modos
fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

for i in range(3):
    mode_shape = vecs[:, i]
    u = euler_cromer_mode(omega[i], mode_shape)

    axs[i].plot(t, u[0, :], label='Massa A')
    axs[i].plot(t, u[1, :], label='Massa B')
    axs[i].plot(t, u[2, :], label='Massa C')
    axs[i].set_title(f'Modo {i+1} (ω = {omega[i]:.4f} rad/s)')
    axs[i].set_ylabel('Deslocamento relativo')
    axs[i].legend()
    axs[i].grid(True)

axs[-1].set_xlabel('Tempo (s)')
plt.tight_layout()
plt.show()
