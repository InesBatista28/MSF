import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros
g = 9.80665
t0 = 0.0
tf = 4.0
dt = 0.01
vx0 = 0.0
x0 = 0.0
y0 = 0.1

# Funções para a pista reta 
def y_func_reta(x: float) -> float:
    return 0.1 - 0.05 * x if x < 2 else 0.0

def dydx_func_reta(x: float) -> float:
    return -0.05 if x < 2 else 0.0

# Funções para a pista curva
def y_func_curva(x: float) -> float:
    return 0.025 * (x - 2)**2 if x < 2 else 0.0

def dydx_func_curva(x: float) -> float:
    return 0.05 * (x - 2) if x < 2 else 0.0



# Função para simulação de movimento
def simular_pista(func_y, func_dydx):
    # Inicializando variáveis
    t = np.arange(t0, tf, dt)
    n = len(t)
    x = np.zeros(n)
    vx = np.zeros(n)
    y = np.zeros(n)
    ax = np.zeros(n)

    x[0] = x0
    vx[0] = vx0
    y[0] = y0

    # Método de Euler-Cromer
    for i in range(n - 1):
        ax[i] = -g * func_dydx(x[i])  # Aceleração
        vx[i + 1] = vx[i] + ax[i] * dt  # Velocidade
        x[i + 1] = x[i] + vx[i + 1] * dt  # Posição
        y[i + 1] = func_y(x[i + 1])  # Altura

        if x[i + 1] >= 2.5:
            break  # Interrompe quando atingir x = 2.5

    return x[:i+2], y[:i+2], vx[:i+2], t[:i+2]

# Simulações para a pista reta e curva
x_reta, y_reta, vx_reta, t_reta = simular_pista(y_func_reta, dydx_func_reta)
x_curva, y_curva, vx_curva, t_curva = simular_pista(y_func_curva, dydx_func_curva)

# Criando a animação
fig, ax = plt.subplots()
line_reta, = ax.plot([], [], 'b-', label="Pista Reta")
line_curva, = ax.plot([], [], 'r-', label="Pista Curva")
ball_reta, = ax.plot([], [], 'bo', label="Bola (Pista Reta)")
ball_curva, = ax.plot([], [], 'ro', label="Bola (Pista Curva)")

ax.set_xlim(0, 2.5)
ax.set_ylim(0, 0.2)
ax.set_xlabel('Distância (m)')
ax.set_ylabel('Altura (m)')
ax.set_title('Animação do Movimento da Bola')

def init():
    line_reta.set_data([], [])
    line_curva.set_data([], [])
    ball_reta.set_data([], [])
    ball_curva.set_data([], [])
    return line_reta, line_curva, ball_reta, ball_curva

def update(frame):
    # Atualiza a posição da bola para a pista reta
    line_reta.set_data(x_reta[:frame], y_reta[:frame])
    line_curva.set_data(x_curva[:frame], y_curva[:frame])

    # Atualiza as posições das bolas (agora como sequências de tamanho 1)
    ball_reta.set_data([x_reta[frame]], [y_reta[frame]])
    ball_curva.set_data([x_curva[frame]], [y_curva[frame]])

    return line_reta, line_curva, ball_reta, ball_curva


ani = FuncAnimation(fig, update, frames=len(t_reta), init_func=init, blit=True, interval=20)

plt.legend()
plt.tight_layout()
plt.show()
