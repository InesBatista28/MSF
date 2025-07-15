import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
m = 1.0       # massa (kg)
k = 1.0       # constante da mola (N/m)
b = 0.16      # coeficiente de amortecimento (kg/s)
F0 = 2.0      # amplitude da força externa (N)
w_f = 2.0     # frequência angular da força externa (rad/s)

# Configurações da simulação    
t_max = 100
dt = 0.01
n = int(t_max / dt)
t = np.linspace(0, t_max, n)

# Função para resolver numericamente a equação diferencial (método de Euler)
def resolver_movimento(x0, v0, w_f):
    x = np.zeros(n)
    v = np.zeros(n)
    x[0] = x0
    v[0] = v0
    for i in range(n - 1):
        a = (-k * x[i] - b * v[i] + F0 * np.cos(w_f * t[i])) / m
        v[i + 1] = v[i] + a * dt
        x[i + 1] = x[i] + v[i + 1] * dt
    return x, v

# Função para encontrar picos (máximos locais)
def encontrar_picos(x, t, inicio):
    picos_t = []
    picos_val = []
    for i in range(inicio + 1, len(x) - 1):
        if x[i] > x[i - 1] and x[i] > x[i + 1]:
            picos_t.append(t[i])
            picos_val.append(x[i])
    return np.array(picos_t), np.array(picos_val)

# Alinea a: Lei do movimento com x0 = 4 m, v0 = 0
x_a, v_a = resolver_movimento(4.0, 0.0, w_f)

# Alinea b: Amplitude e período no regime estacionário
indice_transiente = int(0.8 * n)
picos_t_a, picos_val_a = encontrar_picos(x_a, t, indice_transiente)
amplitude_a = np.mean(np.abs(picos_val_a))
periodo_a = np.mean(np.diff(picos_t_a)) if len(picos_t_a) > 1 else np.nan

# Alinea c: Amplitude em função da frequência forçada
frequencias = np.linspace(0.2, 2.0, 50)
amplitudes = []

for w in frequencias:
    x, v = resolver_movimento(4.0, 0.0, w)
    picos_t, picos_val = encontrar_picos(x, t, indice_transiente)
    if len(picos_val) > 0:
        amp = np.mean(np.abs(picos_val))
    else:
        amp = 0
    amplitudes.append(amp)

# Gráficos
plt.figure(figsize=(14, 6))

# Gráfico da alínea a: posição vs tempo
plt.subplot(1, 2, 1)
plt.plot(t, x_a)
plt.xlabel("Tempo (s)")
plt.ylabel("Posição x(t) (m)")
plt.title("Lei do Movimento (x₀ = 4 m, v₀ = 0 m/s)")
plt.grid(True)

# Gráfico da alínea c: amplitude vs frequência
plt.subplot(1, 2, 2)
plt.plot(frequencias, amplitudes, marker='o')
plt.xlabel("Frequência forçada ω (rad/s)")
plt.ylabel("Amplitude (m)")
plt.title("Amplitude vs Frequência forçada")
plt.grid(True)

plt.tight_layout()
plt.show()

# Resultados da alínea b
print(f"Amplitude no regime estacionário: {amplitude_a:.4f} m")
print(f"Período no regime estacionário: {periodo_a:.4f} s")
