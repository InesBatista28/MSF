import numpy as np
import matplotlib.pyplot as plt

k = 1                
alpha = -0.01         
m = 1                  
dt = 0.001       
t_max = 50            
n = int(t_max / dt)   

def Ep(x):
    return 0.5 * k * x**2 + alpha * x**4

def simula_movimento(x0, v0):
    x = np.zeros(n)
    v = np.zeros(n)
    t = np.linspace(0, t_max, n)
    
    x[0] = x0
    v[0] = v0
    
    for i in range(n-1):
        a = (-k * x[i] - 3 * alpha * x[i]**3) / m
        v[i+1] = v[i] + a * dt
        x[i+1] = x[i] + v[i+1] * dt
    
    return t, x, v

# Função para calcular o período aproximado baseado nos picos da posição
def calcula_periodo(t, x):
    indices_pico = []
    for i in range(1, len(x)-1):
        if x[i-1] < x[i] and x[i] > x[i+1] and t[i] > 1:
            indices_pico.append(i)
            if len(indices_pico) >= 2:
                break
    if len(indices_pico) >= 2:
        T = t[indices_pico[1]] - t[indices_pico[0]]
        return T
    else:
        return float('nan')



x_vals = np.linspace(-3, 3, 500)
Ep_vals = Ep(x_vals)
E_total = 1 

plt.figure(figsize=(8,5))
plt.plot(x_vals, Ep_vals, label='Energia Potencial $E_p(x)$')
plt.axhline(E_total, color='red', linestyle='--', label='Energia Total = 1 J')
plt.xlabel('Posição $x$ (m)')
plt.ylabel('Energia Potencial (J)')
plt.title('Energia Potencial do Oscilador Cúbico')
plt.legend()
plt.grid()
plt.show()



print("Alínea b) Simulação para x0=1.3 m, v0=0 m/s")
t_b, x_b, v_b = simula_movimento(1.3, 0)
# Energia mecânica total (constante)
E_mec_b = Ep(x_b[0]) + 0.5 * m * v_b[0]**2

# Limites do movimento
x_min_b = np.min(x_b)
x_max_b = np.max(x_b)

# Período
T_b = calcula_periodo(t_b, x_b)
f_b = 1/T_b if not np.isnan(T_b) else float('nan')

print(f" Energia mecânica total: {E_mec_b:.4f} J")
print(f" Movimento entre x = {x_min_b:.4f} m e x = {x_max_b:.4f} m")
print(f" Período aproximado: {T_b:.4f} s")
print(f" Frequência aproximada: {f_b:.4f} Hz" if not np.isnan(f_b) else " Frequência indefinida")

plt.figure(figsize=(8,4))
plt.plot(t_b, x_b, label='Posição $x(t)$')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Lei do Movimento para x0=1.3 m, v0=0')
plt.grid()
plt.legend()
plt.show()




print("Alínea c) Simulação para x0=2.9 m, v0=0 m/s")
t_c, x_c, v_c = simula_movimento(2.9, 0)
E_mec_c = Ep(x_c[0]) + 0.5 * m * v_c[0]**2
x_min_c = np.min(x_c)
x_max_c = np.max(x_c)

T_c = calcula_periodo(t_c, x_c)
f_c = 1/T_c if not np.isnan(T_c) else float('nan')

print(f" Energia mecânica total: {E_mec_c:.4f} J")
print(f" Movimento entre x = {x_min_c:.4f} m e x = {x_max_c:.4f} m")
print(f" Período aproximado: {T_c:.4f} s")
print(f" Frequência aproximada: {f_c:.4f} Hz" if not np.isnan(f_c) else " Frequência indefinida")

plt.figure(figsize=(8,4))
plt.plot(t_c, x_c, label='Posição $x(t)$')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Lei do Movimento para x0=2.9 m, v0=0')
plt.grid()
plt.legend()
plt.show()
