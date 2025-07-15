import numpy as np
import matplotlib.pyplot as plt

m = 0.25
k = 1
b = 0.1
x0 = 0.4
v0 = 0
t_max = 20
dt = 0.01
n = int(t_max / dt)
t = np.linspace(0, t_max, n)

x = np.zeros(n)
v = np.zeros(n)
x[0] = x0
v[0] = v0

# a) Lei do movimento (Método de Euler)
for i in range(n-1):
    a = (-k * x[i] - b * v[i]) / m
    v[i+1] = v[i] + a * dt
    x[i+1] = x[i] + v[i+1] * dt

plt.plot(t, x)
plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.title("Oscilador Amortecido: Posição vs Tempo")
plt.grid()
plt.show()


# b) Interpolação de Lagrange para encontrar máximos e mínimos
def encontra_extremos(t, x):
    extremos_t = []
    extremos_x = []

    for i in range(2, len(x) - 2):
        if (x[i-1] < x[i] > x[i+1]) or (x[i-1] > x[i] < x[i+1]):
            # Interpolação de Lagrange com 5 pontos
            ts = t[i-2:i+3]
            xs = x[i-2:i+3]
            coef = np.polyfit(ts, xs, 4)
            p = np.poly1d(coef)
            dp = p.deriv()
            roots = dp.r
            roots = roots[np.isreal(roots)].real
            for r in roots:
                if ts[0] <= r <= ts[-1]:
                    extremos_t.append(r)
                    extremos_x.append(p(r))
    return np.array(extremos_t), np.array(extremos_x)

ext_t, ext_x = encontra_extremos(t, x)

plt.plot(t, x, label='x(t)')
plt.plot(ext_t, ext_x, 'ro', label='Máx/Mín')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Extremos locais por Interpolação de Lagrange')
plt.grid()
plt.legend()
plt.show()


# c) Ajuste linear de log(amplitude) vs tempo
# Usar apenas máximos (valores positivos)
max_indices = ext_x > 0
t_maximos = ext_t[max_indices]
x_maximos = ext_x[max_indices]

log_amp = np.log(x_maximos)

# Ajuste linear
coef, cov = np.polyfit(t_maximos, log_amp, 1, cov=True)
declive = coef[0]
intercepto = coef[1]
erro_declive = np.sqrt(cov[0, 0])

plt.plot(t_maximos, log_amp, 'o', label='log(Amplitude)')
plt.plot(t_maximos, np.polyval(coef, t_maximos), 'r-', label=f'Ajuste: y = {declive:.4f}x + {intercepto:.4f}')
plt.xlabel('Tempo (s)')
plt.ylabel('log(Amplitude)')
plt.title('Decaimento Exponencial da Amplitude')
plt.grid()
plt.legend()
plt.show()

print("Declive do ajuste linear:", round(declive, 5))
print("Erro do declive:", round(erro_declive, 5))
