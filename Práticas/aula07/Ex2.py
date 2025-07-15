import numpy as np
import matplotlib.pyplot as plt

g=9.80665
t0 = 0.0 
tf = 4.0 
dt = 0.001 
vx0 = 0.0 
x0 = 0.0 
y0 = 0.1

# Trajetória y(x)  MUDA A FORMA DA PISTA EM RELAÇÃO A EX1.PY
# y(x) = 0.025 * (x - 2)**2 para x < 2, de outra forma y(x) = 0
def y_func(x: float) -> float:
    return 0.025 * (x - 2)**2 if x < 2.0 else 0.0


# Derivada de y em ordem a x
# dy/dx = 0.05 * (x - 2) para x < 2, de outra forma dy/dx = 0
def dydx_func(x: float) -> float:
    return 0.05 * (x - 2) if x < 2.0 else 0.0

t = np.arange(t0, tf, dt)
ax = np.zeros(np.size(t))
vx = np.zeros(np.size(t))
vx[0] = vx0
x = np.zeros(np.size(t))
x[0] = x0
y = np.zeros(np.size(t))
y[0] = y0

for i in range(np.size(t) - 1):
    ax[i] = -g * dydx_func(x[i])

    # Método de Euler-Cromer
    vx[i + 1] = vx[i] + ax[i] * dt
    x[i + 1] = x[i] + vx[i + 1] * dt
    y[i + 1] = y_func(x[i+1])

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('x', color=color)
ax1.plot(t[x<2.5], x[x<2.5], color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx() # partilhar eixo horizontal
color = 'tab:red'
ax2.set_ylabel('y', color=color)
ax2.plot(t[x<2.5], y[x<2.5], color=color)
ax2.tick_params(axis='y', labelcolor=color)
fig.tight_layout()
plt.show()



x2 = x
y2 = y
vx2 = vx
i25 = np.size(x[x<=2.5])
v25 = vx[i25]
t25 = t[i25]
print("Quando x = 2.5 m, a velocidade é v = {0:.5f} m/s²".format(v25))
print("Quando x = 2.5 m, o tempo decorrido é t = {0:.5f} s".format(t25))



#Velociade diminui à medida que a altura aumenta
plt.plot(y[:i25+1], vx[:i25+1], 'r-', label="Pista Curva")
plt.xlabel('Altura y (m)')
plt.ylabel('Velocidade vx (m/s)')
plt.title('Velocidade vs Altura')
plt.legend()
plt.tight_layout()
plt.show()


