import numpy as np
import matplotlib.pyplot as plt

# Constantes
m = 1.0        # massa (kg)
k = 1.0        # constante da mola (N/m)
b = 0.05       # coeficiente de amortecimento (kg/s)
F0 = 7.5       # amplitude da força externa (N)
w_f = 1.0      # frequência angular da força externa (rad/s)

# Tempo
t_max = 100
dt = 0.01
n = int(t_max / dt)
t = np.linspace(0, t_max, n)

# Função para resolver EDO com o método de Euler
def resolver_movimento(x0, v0):
    x = np.zeros(n)
    v = np.zeros(n)
    x[0] = x0
    v[0] = v0
    for i in range(n - 1):
        a = (-k * x[i] - b * v[i] + F0 * np.cos(w_f * t[i])) / m
        v[i+1] = v[i] + a * dt
        x[i+1] = x[i] + v[i+1] * dt
    return x, v

# Casos a) e c)
x1, v1 = resolver_movimento(4.0, 0.0)      # alínea a
x2, v2 = resolver_movimento(-2.0, -4.0)    # alínea c

# Função para calcular amplitude e período no regime estacionário
def amplitude_periodo(x, t):
    # Encontrar picos (máximos locais) manualmente
    picos = []
    for i in range(1, len(x) - 1):
        if x[i-1] < x[i] and x[i] > x[i+1]:
            picos.append(i)
    
    tempos = t[picos]
    amplitudes = np.abs(x[picos])
    
    # Calcular o período
    if len(tempos) > 1:
        periodo = np.mean(np.diff(tempos))
    else:
        periodo = np.nan
    
    # Amplitude média
    amplitude = np.mean(amplitudes)
    
    return amplitude, periodo, tempos, amplitudes

# b) e d)
amp1, T1, tempos1, amps1 = amplitude_periodo(x1, t)
amp2, T2, tempos2, amps2 = amplitude_periodo(x2, t)

# e) Energia mecânica (manual)
def energia_mec(x, v):
    Ep = 0.5 * k * x**2
    Ec = 0.5 * m * v**2
    return Ep + Ec

E1 = energia_mec(x1, v1)
E2 = energia_mec(x2, v2)

# Plot geral
plt.figure(figsize=(14, 9))

# Movimento
plt.subplot(3,1,1)
plt.plot(t, x1, label="x(t) - caso a")
plt.plot(t, x2, label="x(t) - caso c", linestyle='--')
plt.title("Lei do Movimento")
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.legend()
plt.grid(True)

# Energia
plt.subplot(3,1,2)
plt.plot(t, E1, label="Energia mecânica - caso a")
plt.plot(t, E2, label="Energia mecânica - caso c", linestyle='--')
plt.title("Energia Mecânica")
plt.xlabel("Tempo (s)")
plt.ylabel("Energia (J)")
plt.legend()
plt.grid(True)

# Amplitudes (após transiente)
plt.subplot(3,1,3)
plt.plot(tempos1, amps1, "o-", label="Amplitudes - caso a")
plt.plot(tempos2, amps2, "s--", label="Amplitudes - caso c")
plt.title("Amplitude vs Tempo (Regime Estacionário)")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude (m)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


print(f"Alínea b) - Caso a:")
print(f"Amplitude média ≈ {amp1:.4f} m")
print(f"Período ≈ {T1:.4f} s\n")

print(f"Alínea d) - Caso c:")
print(f"Amplitude média ≈ {amp2:.4f} m")
print(f"Período ≈ {T2:.4f} s\n")

print(f"Alínea e) - Energia é constante?")
print("Não. Energia oscila e varia com o tempo devido à força externa e ao amortecimento.")
