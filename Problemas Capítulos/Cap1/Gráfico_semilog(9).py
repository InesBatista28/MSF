import numpy as np
import matplotlib.pyplot as plt

tempo = np.arange(0, 50, 5)   
atividade = np.array([9.676, 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119])  

plt.scatter(tempo, atividade, color='blue', label="Medições")
plt.xlabel("Tempo (dias)")
plt.ylabel("Atividade (mCi)")
plt.title("Decaimento da Atividade ao Longo do Tempo")
plt.legend()
plt.show()

log_atividade = np.log(atividade)

plt.figure(figsize=(8, 5))
plt.scatter(tempo, log_atividade, color='green', label="Medições")

p, cov = np.polyfit(tempo, log_atividade, 1, cov=True)
declive = p[0]
incerteza_declive = np.sqrt(cov[0, 0])  

plt.plot(tempo, declive * tempo + p[1], color='red', label=f"Ajuste Linear (m={declive:.4f} ± {incerteza_declive:.4f})")
plt.xlabel("Tempo (dias)")
plt.ylabel("log(Atividade)")
plt.title("Gráfico Semilog")
plt.legend()
plt.show()

print(f"Declive (m): {declive:.4f} ± {incerteza_declive:.4f} dias⁻¹")
