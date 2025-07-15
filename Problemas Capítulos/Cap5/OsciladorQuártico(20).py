import numpy as np
import matplotlib.pyplot as plt

m = 1.0       # massa (kg)
k = 1.0       # constante elástica (N/m)
b = 0.05      # coeficiente de amortecimento (kg/s)
alpha = 0.002 # não-linearidade quártica (N/m^2)
F0 = 7.5      # força externa (N)
w_f = 1.0     # frequência angular (rad/s)

# Parâmetros de simulação
t_max = 100
dt = 0.01
n = int(t_max / dt)
t = np.linspace(0, t_max, n)

# Função para resolver a equação do movimento
def resolver_movimento(x0, v0):
    x = np.zeros(n)
    v = np.zeros(n)
    x[0], v[0] = x0, v0
    for i in range(n - 1):
        f_ext = F0 * np.cos(w_f * t[i])
        f_spring = -k * x[i] * (1 + 2 * alpha * x[i]**2)
        f_damp = -b * v[i]
        a = (f_spring + f_damp + f_ext) / m
        v[i+1] = v[i] + a * dt
        x[i+1] = x[i] + v[i+1] * dt
    return x, v

# Função para detectar picos (máximos locais)
def encontrar_picos(x, t, inicio=0.8):
    i_start = int(inicio * len(x))
    picos_t, picos_val = [], []
    for i in range(i_start + 1, len(x) - 1):
        if x[i] > x[i - 1] and x[i] > x[i + 1]:
            picos_t.append(t[i])
            picos_val.append(x[i])
    return np.array(picos_t), np.array(picos_val)

# Energia mecânica total
def energia_mecanica(x, v):
    E_pot = 0.5 * k * x**2 * (1 + alpha * x**2)
    E_cin = 0.5 * m * v**2
    return E_pot + E_cin

# Alinea a)
x1, v1 = resolver_movimento(3.0, 0.0)
picos_t1, picos_val1 = encontrar_picos(x1, t)
amplitude1 = np.mean(np.abs(picos_val1))
periodo1 = np.mean(np.diff(picos_t1)) if len(picos_t1) > 1 else np.nan

# Alinea c)
x2, v2 = resolver_movimento(-2.0, -4.0)
picos_t2, picos_val2 = encontrar_picos(x2, t)
amplitude2 = np.mean(np.abs(picos_val2))
periodo2 = np.mean(np.diff(picos_t2)) if len(picos_t2) > 1 else np.nan

# Energia mecânica
energia1 = energia_mecanica(x1, v1)
energia2 = energia_mecanica(x2, v2)

# Gráficos
plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
plt.plot(t, x1)
plt.title("a) Movimento (x₀=3, v₀=0)")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição x(t)")
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(t, x2)
plt.title("c) Movimento (x₀=-2, v₀=-4)")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição x(t)")
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(t, energia1, label="Energia (x₀=3)")
plt.plot(t, energia2, label="Energia (x₀=-2)")
plt.title("e) Energia mecânica total")
plt.xlabel("Tempo (s)")
plt.ylabel("Energia (J)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

print("b) Amplitude (x₀=3):", amplitude1)
print("   Período:", periodo1)
print("d) Amplitude (x₀=-2):", amplitude2)
print("   Período:", periodo2)
