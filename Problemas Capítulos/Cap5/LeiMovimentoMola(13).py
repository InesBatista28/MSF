import matplotlib.pyplot as plt
import numpy as np

k = 1
m = 1
x0 = 4
v0 = 0
t = 30          #tempo total de simulação
dt = 0.01

# Como a força -k x(t) é igual à resultante vem que é igual a m a(t)
# Número de passos durante o tempo de simulação definido
n = int(t / dt)


# Inicialização dos vetores de tempo, posição e velocidade
t = np.linspace(0, t, n)
x = np.zeros(n)
v = np.zeros(n)

# Condições iniciais
x[0] = x0
v[0] = v0

# Método de Euler para resolver a EDO: ma(t) = -kx(t)
for i in range(n-1):
    a = -k/m * x[i]                     
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i+1] * dt

# a) Gráfico da lei do movimento
plt.plot(t, x)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Lei do movimento: oscilador harmônico simples')
plt.grid(True)
plt.show()

# b) Amplitude e período
amplitude = np.max(np.abs(x))

# Encontrar picos (máximos locais) manualmente
indices_pico = []
for i in range(1, n-1):
    if x[i-1] < x[i] and x[i] > x[i+1]:
        indices_pico.append(i)

if len(indices_pico) >= 2:
    periodo = t[indices_pico[1]] - t[indices_pico[0]]
else:
    periodo = float('nan')  

print(f"Amplitude aproximada: {amplitude:.2f} m")
print(f"Período aproximado: {periodo:.3f} s")


# c) Energia mecânica: E = Ec + Ep
# Ec = 0.5 * m * v², Ep = 0.5 * k * x²
energia_cinetica = 0.5 * m * v**2
energia_potencial = 0.5 * k * x**2
energia_mecanica = energia_cinetica + energia_potencial

plt.plot(t, energia_cinetica, label='Energia Cinética (J)', linestyle='--')
plt.plot(t, energia_potencial, label='Energia Potencial (J)', linestyle='-.')
plt.plot(t, energia_mecanica, label='Energia Mecânica Total (J)', linewidth=2)
plt.xlabel('Tempo (s)')
plt.ylabel('Energia (J)')
plt.title('Energia mecânica ao longo do tempo')
plt.legend()
plt.grid(True)
plt.show()

print(f"Energia mecânica total média: {np.mean(energia_mecanica):.2f} J")
print("A energia mecância é constante ao longo do tempo.")