import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t0 = 0.0
tf = 1.0
dt = 0.001
v0 = 2.0 * np.pi
x0 = 1.0

G = 4.0 * np.pi **2

t = np.arange(t0, tf, dt)
a = np.zeros([np.size(t), 2])

v = np.zeros([np.size(t), 2])
v[0, :] = np.array([0, v0])

r = np.zeros([np.size(t), 2])
r[0, :] = np.array([x0, 0.0])


#Atualiza a velocidade primeiro, só depois a posição 
#conseguimos orbitas fechadas pois conserva melhor a energia 
for i in range(np.size(t) - 1):
    a[i, :] = -G * r[i, :]
    v[i + 1, :] = v[i, :] + a[i, :] * dt
    r[i + 1, :] = r[i, :] + v[i + 1, :] * dt

#Criar a animação
fig, ax = plt.subplots()

terra = ax.plot(r[:, 0], r[:, 1], 'o')[0]
ax.set(xlim = [-2, 2], ylim = [-2,2])

def update(frame):
    terra.set_xdata(r[frame, 0])
    terra.set_ydata(r[frame, 1])

ani = FuncAnimation(fig = fig, func = update, frames = 100, interval = 30)


plt.plot(r[:, 0], r[:, 1], 'b-')
plt.xlabel("Posição em x (AU)")
plt.ylabel("Posição em y (AU)")
plt.show()

print("Pelo gráfico é possível garantir que se conseguem obter órbitas fechadas")
print("Se se alterar o valor da velocidade inicial, mesmo assim continuam a existir elipses")