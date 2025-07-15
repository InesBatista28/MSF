import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
k = 1.0       
k_p = 0.5     
m = 1.0       
dt = 0.01     
t_max = 50    
n_steps = int(t_max / dt)
t = np.linspace(0, t_max, n_steps)

K = np.array([[1.5, -0.5, 0],[-0.5, 1.0, -0.5],[0, -0.5, 1.5]])
w2, modos = np.linalg.eigh(K)
w = np.sqrt(w2)



def simular_modo(v_inicial):
    u = np.zeros((3, n_steps))   # posições das massas
    v = np.zeros((3, n_steps))   # velocidades
    u[:, 0] = v_inicial          # condição inicial: modo normal
    
    for i in range(1, n_steps):
        # Força restauradora: F = -K * u
        F = -K @ u[:, i-1]
        # Atualiza velocidade
        v[:, i] = v[:, i-1] + (F/m) * dt
        # Atualiza posição
        u[:, i] = u[:, i-1] + v[:, i] * dt

    return u



for j in range(3):
    u = simular_modo(modos[:, j])
    plt.figure(figsize=(10, 4))
    plt.plot(t, u[0], label='Massa A')
    plt.plot(t, u[1], label='Massa B')
    plt.plot(t, u[2], label='Massa C')
    plt.title(f"Modo Normal {j+1} - Frequência ω ≈ {w[j]:.2f} rad/s")
    plt.xlabel('Tempo (s)')
    plt.ylabel('Posição (m)')
    plt.legend()
    plt.grid()
    plt.show()
