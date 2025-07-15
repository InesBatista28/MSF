import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
N = 5           # número de massas
k = 1.0         # constante elástica (N/m)
m = 1.0         # massa (kg)
dt = 0.01       # passo de tempo
t_max = 50      # tempo total
steps = int(t_max / dt)
t = np.linspace(0, t_max, steps)

# Frequência angular teórica para modo l
def omega_l(l, N):
    return 2 * np.sqrt(k/m) * np.sin(l * np.pi / (2 * (N+1)))

# Condição inicial para modo normal l
def posicao_inicial(l, N, A=1.0):
    return A * np.sin(np.pi * np.arange(1, N+1) * l / (N+1))

# Simulação via Euler-Cromer
def simular(l):
    u = np.zeros((N, steps))     # posições
    v = np.zeros((N, steps))     # velocidades
    u[:, 0] = posicao_inicial(l, N)

    for i in range(1, steps):
        F = np.zeros(N)
        for j in range(N):
            if j == 0:
                F[j] = -k * u[j, i-1] - k * (u[j, i-1] - u[j+1, i-1])
            elif j == N-1:
                F[j] = -k * u[j, i-1] - k * (u[j, i-1] - u[j-1, i-1])
            else:
                F[j] = -k * (u[j, i-1] - u[j-1, i-1]) - k * (u[j, i-1] - u[j+1, i-1])

        v[:, i] = v[:, i-1] + (F/m) * dt
        u[:, i] = u[:, i-1] + v[:, i] * dt

    return u

# Plotar resultados para os modos l = 1 até N
for l in range(1, N+1):
    u = simular(l)
    plt.figure(figsize=(10, 4))
    for j in range(N):
        plt.plot(t, u[j], label=f'Massa {j+1}')
    plt.title(f"Modo Normal l={l}, Frequência ω ≈ {omega_l(l,N):.2f} rad/s")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.grid()
    plt.legend()
    plt.show()
