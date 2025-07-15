import numpy as np
import matplotlib.pyplot as plt

#simular o movimeto de duas esferas sujeitas às seguintes forças (método de euler)
def acc_toque(dx,d):
    # calcular a aceleração de uma esfera devido ao contacto com a esfera à sua direita
    k = 1e7
    q = 2.0
    if dx<d:
        a = (-k*abs(dx-d)**q)/m
    else:
        a = 0.0
    return a

def acc_i(i,x):
    #calcular a aceleração de esfera i, cuja posicao de equilibrio é d*i
    a = 0

    if i>0: # a primeira esfera não tem vizinho à sua esquerda
        a -= acc_toque(x[i] - x[i-1],d)
    if i < (N-1): # a última esfera não tem vizinho à sua direita
        a += acc_toque(x[i+1] - x[i], d)

    # aceleração de gravidade, afeta todas as esferas
    a -= g*(x[i]-d*i)/l
    return a


t0 = 0.0 
tf = 5.0 
dt = 0.001 

t = np.arange(t0, tf, dt)  #variáveis tempo
Nt = np.size(t)

N = 4
d = 0.1 
l = 10 * d
m = 0.3 
g = 9.8   
k = 1e7 #constante de forca elastica [N/m^2]
x0 = np.arange(0, N, 1) * d #posições 

#inicializar das granzedas físicas
x_arr = np.zeros((N, Nt)) 
v_arr = np.zeros((N, Nt)) 
a_arr = np.zeros((N, Nt)) 

#condicoes iniciais
x_arr[:, 0] = x0 #posições iniciais de equilibrio da esfera 
x_arr[0, 0] = - 5 * d #altera a posição da primeira esfera - inicia o movimento do sistema
v_arr[:, 0] = np.zeros(N) #velocidade inicial as esferas 

#método de euler 
for j in range(Nt - 1): #loop no tempo
    for i in range(N): #loop nas esferas
        a_arr[i, j] = acc_i(i, x_arr[:, j])  #acelaração da esfersa i no tempo j 
    
    v_arr[:, j + 1] = v_arr[:, j] + a_arr[:, j] * dt  #atualiza a velocidade das mesmas com a aceleração
    x_arr[:, j + 1] = x_arr[:, j] + v_arr[:, j + 1] * dt  #atualiza a posição com a velocidade


for i in range(N):  #percorrer ambas as esferas 
    plt.plot(t, x_arr[i, :], label=f'Esfera {i+1}')  #escolhe uma esfera e plota a sua posição

plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Posição, x [m]")
plt.legend()
plt.show()

#calculo do momento total em cada instante
p_arr = m * v_arr  #matriz que representa o movimento linear de cada esfera em cada instante 
p_tot = p_arr[0, :] + p_arr[1, :]  #soma dos momentos individuais das esferas para saber o momento total do sistema 

plt.plot(t, p_arr[0, :], color='orange', label='Esfera 1')
plt.plot(t, p_arr[1, :], color='green', label='Esfera 2')
plt.plot(t, p_tot, color='purple', linestyle='--', label='Momento total')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Momento linear, p [kg·m/s]")
plt.legend()
plt.show()


#calculo da energia cinética e potencial em cada instante 
E_c = p_tot**2 / (2 * m)  #(movimento linear total)**2 / (2*massa)
E_p = m * g * (x_arr[0, :] - x0[0])**2 / (2 * l)
E_p += m * g * (x_arr[1, :] - x0[1])**2 / (2 * l)

plt.plot(t, E_c, color='gold', label='Energia cinética')
plt.plot(t, E_p, color='teal', label='Energia potencial')
plt.xlabel("Tempo decorrido, t [s]")
plt.ylabel("Energia [J]")
plt.show()

