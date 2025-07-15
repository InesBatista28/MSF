import numpy as np
import matplotlib.pyplot as plt

#bola de futebol chutada com ângulo em relação horizontal
#considerar apenas peso = sem resistência do ar
v0 = 27.78  
theta_deg = 10
theta = np.radians(theta_deg)
g = 9.8  

# Componentes da velocidade inicial
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

#função dá a altura da bola em função da distância horizontal
def y_de_x(x):
    return x * np.tan(theta) - (g * x**2) / (2 * v0**2 * np.cos(theta)**2)

# Geração dos pontos
x_vals = np.linspace(0, (v0**2 * np.sin(2*theta)) / g, 500) #cria um vetor de 500 valores que variam desde o 0 até à distância máxima atinguida pela bola
y_vals = y_de_x(x_vals) #aplica a função y_de_x para cada valor de x = obtem a altura correspondente

#cálculo da altura máxima atinguida pela bola
y_max = (v0y**2) / (2 * g)  #a altura máxima ocorre quando a velocidade é nula
print(f"A altura máxima atingida pela bola é {y_max:.2f} m")
t_max = v0y / g
print(f"O tempo máximo de subida é {t_max:.2f} s")

#alcance da bola (Distância percorrida)
t_total = 2 * t_max #tempo total de subida e descida
alcance = v0 * np.cos(theta) * t_total
print(f"Tempo total de voo: {t_total:.2f} s")
print(f"Alcance horizontal: {alcance:.2f} m")

plt.plot(x_vals, y_vals)
plt.title("Trajetória da bola de futebol (sem resistência do ar)")
plt.xlabel("Distância horizontal (m)")
plt.axhline(y_max, color='r', linestyle='--', label=f"Altura Máx: {y_max:.2f} m")
plt.axvline(v0x * t_max, color='g', linestyle='--', label=f"Suposto Instante: {t_max:.2f} s")
plt.ylabel("Altura (m)")
plt.grid(True)
plt.legend()
plt.show()


