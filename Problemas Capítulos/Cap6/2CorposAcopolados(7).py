import numpy as np
import matplotlib.pyplot as plt

# --- Parâmetros do sistema ---
k = 1.0       # constante das molas externas (N/m)
k_p = 0.5     # constante da mola entre os corpos (N/m)
m = 1.0       # massa de cada corpo (kg)
xA_eq = 1.0   # posição de equilíbrio do corpo A
xB_eq = 1.2   # posição de equilíbrio do corpo B

# --- Parâmetros de simulação ---
dt = 0.01             # passo de tempo
T_total = 50.0        # duração total da simulação
N = int(T_total / dt) # número de passos
t = np.linspace(0, T_total, N)

# --- Simulador com método de Euler ---
def simulate_motion(xA0, vA0, xB0, vB0):
    xA = np.zeros(N)
    vA = np.zeros(N)
    xB = np.zeros(N)
    vB = np.zeros(N)

    xA[0], vA[0] = xA0, vA0
    xB[0], vB[0] = xB0, vB0

    for i in range(N - 1):
        # Forças elásticas
        FA = -k * (xA[i] - xA_eq) - k_p * ((xA[i] - xA_eq) - (xB[i] - xB_eq))
        FB = -k * (xB[i] - xB_eq) + k_p * ((xA[i] - xA_eq) - (xB[i] - xB_eq))

        # Acelerações
        aA = FA / m
        aB = FB / m

        # Atualização com Euler
        vA[i+1] = vA[i] + aA * dt
        xA[i+1] = xA[i] + vA[i+1] * dt

        vB[i+1] = vB[i] + aB * dt
        xB[i+1] = xB[i] + vB[i+1] * dt

    return t, xA, xB

# --- Função para estimar período e frequência angular ---
def estimar_periodo(t, x):
    x_centrado = x - np.mean(x)
    picos = []

    for i in range(1, len(x_centrado) - 1):
        if x_centrado[i-1] < x_centrado[i] > x_centrado[i+1]:
            picos.append(t[i])

    picos = np.array(picos)
    if len(picos) < 2:
        return None, None

    periodos = np.diff(picos)
    T_medio = np.mean(periodos)
    omega = 2 * np.pi / T_medio
    return T_medio, omega

# --- Casos iniciais ---
casos = {
    "i":    (xA_eq + 0.05, 0, xB_eq + 0.05, 0),
    "ii":   (xA_eq + 0.05, 0, xB_eq - 0.05, 0),
    "iii":  (xA_eq + 0.05, 0, xB_eq,        0),
}

# --- Simulação e visualização ---
plt.figure(figsize=(12, 8))
resultados = {}

# --- Simular e armazenar resultados ---
for nome, (xA0, vA0, xB0, vB0) in casos.items():
    resultados[nome] = simulate_motion(xA0, vA0, xB0, vB0)

# --- Gráficos separados para cada caso ---
fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)

for idx, (nome, _) in enumerate(casos.items()):
    t, xA, xB = resultados[nome]
    axs[idx].plot(t, xA - xA_eq, label=f'xA - xA_eq ({nome})')
    axs[idx].plot(t, xB - xB_eq, '--', label=f'xB - xB_eq ({nome})')
    axs[idx].set_ylabel("Deslocamento (m)")
    axs[idx].set_title(f"Caso ({nome})")
    axs[idx].grid(True)
    axs[idx].legend()

axs[-1].set_xlabel("Tempo (s)")
plt.tight_layout()
plt.show()

# --- Estimar período e frequência angular para os casos (i) e (ii) ---
t_i, xA_i, _ = resultados["i"]
T_i, omega_i = estimar_periodo(t_i, xA_i - xA_eq)

t_ii, xA_ii, _ = resultados["ii"]
T_ii, omega_ii = estimar_periodo(t_ii, xA_ii - xA_eq)

# --- Mostrar resultados ---
print(f"Caso (i): T ≈ {T_i:.3f} s, ω ≈ {omega_i:.3f} rad/s")
print(f"Caso (ii): T ≈ {T_ii:.3f} s, ω ≈ {omega_ii:.3f} rad/s")
