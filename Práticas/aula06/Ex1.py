import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t0 = 0.0
tf = 10.0            #A volta da Terra ao sol demora 1 ano
dt = 0.001          #No caso de se contar mais do que 1 ano, vai influenciar se as linhas aparecem mais próximas ou não
v0 = 2 * np.pi
x0 = 1.0            #Coordenada x da posicão inicial da Terra que se encontra na posição (1,0)

G = 4.0 * np.pi ** 2            #Constante da gravitação universal [AU^3 / M ano ^ 2]
    

t = np.arange(t0, tf, dt)           #Encontrar o número de intervalos de tempo
a = np.zeros([np.size(t), 2])       #Vetor da aceleração 2D (x,y)

v = np.zeros([np.size(t), 2])       #Vetor da velocidade 2D (x,y)
v[0, :] = np.array([0, v0])

r = np.zeros([np.size(t), 2])       #Vetor da velocidade 2D (x,y)
r[0, :] = np.array([x0, 0.0])

for i in range(np.size(t) - 1):
    a[i, :] = -G * r[i, :] / np.linalg.norm(r[i, :]) ** 3       #np.linanlg é para obter a norma do vetor bidimensional r
    v[i + 1, :] = v[i, :] + a[i, :] * dt
    r[i + 1, :] = r[i, :] + v[i, :] * dt

#Criar a animação
fig, ax = plt.subplots()

#ponto que representa a terra
terra = ax.plot(r[:, 0], r[:, 1], 'o')[0]
ax.set(xlim = [-2, 2], ylim = [-2,2]) #limites do gráfico

def update(frame):
    #recebe o frame e dá update na posição da bolinha 
    terra.set_xdata(r[frame, 0])
    terra.set_ydata(r[frame, 1])

ani = FuncAnimation(fig = fig, func = update, frames = 100, interval = 30)  
#Definimos 100 frames 

#Desenhar trajetória
plt.plot(r[:, 0], r[:, 1], 'b-')
plt.xlabel("Posição em x (AU)")
plt.ylabel("Posição em y (AU)")
plt.show()

print("Como é visível no gráfico, a volta da Terra ao Sol não é fechada")
print("As elipses dependem da velocidade inicial, mas as trajetórias normalmente são curvilíneas abertas")


