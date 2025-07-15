import numpy as np
import matplotlib.pyplot as plt

g = 9.81 
vT = 120 / 3.6  # velocidade terminal em m/s
dt = 0.01  
t_max = 0.4  # tempo máximo de simulação em segundos (simulação curta)
m = 0.057

r = np.array([0.0, 2.0, 3.0])  # posição inicial (x, y, z)
v = np.array([160, 20, -20]) / 3.6  # velocidade inicial em m/s

# Listas para armazenar dados da simulação
trajetoria = [r.copy()]
tempos = [0]
velocidades = [v.copy()]
posicoes = [r.copy()]
Ep = [0]  # Energia Potencial
Ec = [0]  # Energia Cinética
Em = [0]  # Energia Mecânica
F_res = [] # Força de resistência do ar

# Simulação com método de Euler
t = 0  #Começa no instante zero
while r[2] > 0 and t < t_max:  # simulação só continua enquanto a bola estiver acima do chão e enquanto o t máximo não for atingido
    norm_v = np.linalg.norm(v) #norma da velocidade para a resistência do ar
    a_grav = np.array([0, 0, -g])  #acelaração da gravidade atua apenas no eixo z
    a_resist = - (g / vT**2) * norm_v * v  #modelo da resistência do ar
    a = a_grav + a_resist  #aceleração total = gravitacional + resistência do ar

    F_res.append(m * a_resist)

    # Método de Euler
    v = v + a * dt #atualizar velocidade
    r = r + v * dt #atualizar posição

    # Calcula e guarda as energias 
    Ep.append(m * g * r[2])  # Energia Potencial
    Ec.append(0.5 * m * norm_v**2)  # Energia Cinética
    Em.append(Ep[-1] + Ec[-1])  # Energia Mecânica

    trajetoria.append(r.copy())  #guardar nova posição
    velocidades.append(v.copy()) #guardar nova velocidade
    posicoes.append(r.copy())   #guardar nova posição
    t += dt  #atualizar tempo da simulação 
    tempos.append(t) #guardar novo tempo

# Converter trajetória em arrays para gráfico
trajetoria = np.array(trajetoria)
velocidades = np.array(velocidades)
posicoes = np.array(posicoes)
tempos = np.array(tempos)
tempos = np.array(tempos)
Ep = np.array(Ep)
Ec = np.array(Ec)
Em = np.array(Em)
F_res = np.array(F_res)


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(trajetoria[:, 0], trajetoria[:, 1], trajetoria[:, 2], label='Trajetória da bola')  #desenho da curva da trajetória 
ax.set_xlabel('x (comprimento do campo) [m]')
ax.set_ylabel('y (largura do campo) [m]')
ax.set_zlabel('z (altura) [m]')
ax.set_title('Simulação da Trajetória do Serviço de Ténis')
ax.legend()
plt.show()

ponto_final = trajetoria[-1]
print(f"A bola toca no solo em: x = {ponto_final[0]:.2f} m, y = {ponto_final[1]:.2f} m")




# Cálculo da variação da energia mecânica
variacao = Em[-1] - Em[0]
print(f"A variação de energia mecânica é {variacao:.2f} Joules")


F_res = np.vstack((F_res, F_res[-1]))  # garantir que tem o mesmo tamanho de 'velocidades' + adicionar o valor final
F_dot_v = np.sum(F_res * velocidades, axis=1)  # produto escalar F·v

# Função para integração numérica do produto escalar (regra do trapézio)
def integral(f, intervalo, a, b):
    dt = (intervalo[1] - intervalo[0]) / len(f)
    i_a = int((a - intervalo[0]) / dt)
    i_b = int((b - intervalo[0]) / dt)
    soma = 0.0
    for i in range(i_a, min(i_b, len(f)-1)):
        soma += (f[i] + f[i+1]) / 2.0 * dt
    return soma

# Intervalo total
intervalo = np.array([tempos[0], tempos[-1]])
t1 = 0.2
t2 = 0.4

# Trabalho realizado (W = ∫F·v dt)
W0 = integral(F_dot_v, intervalo, tempos[0], tempos[0])
W1 = integral(F_dot_v, intervalo, tempos[0], t1)
W2 = integral(F_dot_v, intervalo, tempos[0], t2)

print(f"O trabalho realizado pela força resultante de t0 a t0 é {W0:.2f} Joules")
print(f"O trabalho realizado pela força resultante de t0 a t1 é {W1:.2f} Joules")
print(f"O trabalho realizado pela força resultante de t0 a t2 é {W2:.2f} Joules")

# Cálculo do trabalho realizado pela força de resistência do ar (por conservação de energia)
Ec0 = Ec[0]
Ep0 = Ep[0]
Ec1 = Ec[-1]
Ep1 = Ep[-1]

W_res = (Ec1 + Ep1) - (Ec0 + Ep0)
print(f"O trabalho realizado pela força de resistência do ar (via conservação de energia) é {W_res:.2f} Joules")











