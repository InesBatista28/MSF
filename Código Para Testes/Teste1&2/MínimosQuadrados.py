import matplotlib.pyplot as plt
import numpy as np

# Dados experimentais
L = np.array([222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0])  # variável independente (x)
X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])                 # variável dependente (y)

# Gráfico dos pontos
plt.plot(L, X, 's', color="purple", label='Pontos experimentais')
plt.xlabel('L (cm)')
plt.ylabel('X (cm)')

# Função de regressão linear
def lin_reg(x, y):
    assert len(x) == len(y)
    assert len(x) >= 3

    n = len(x)
    sum_xy = np.sum(x * y)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_y2 = np.sum(y**2)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_x2 * sum_y - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)
    r2 = ((n * sum_xy - sum_x * sum_y)**2) / ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

    delta_m = np.abs(m) * np.sqrt(((1 / r2) - 1) / (n - 2))
    delta_b = delta_m * np.sqrt(sum_x2 / n)

    return m, b, r2, delta_m, delta_b

# Cálculo da regressão
m, b, r2, delta_m, delta_b = lin_reg(L, X)

# Reta de regressão
x_fit = np.linspace(min(L), max(L), 100)
y_fit = m * x_fit + b
plt.plot(x_fit, y_fit, '-g', label=f'Regressão linear\ny = {round(m,3)}x + {round(b,3)}')  #reta cujos parametros são m e b

# Informações do gráfico
plt.title(f'Regressão linear\nm = {round(m,4)} ± {round(delta_m,4)} ; b = {round(b,4)} ± {round(delta_b,4)} ; r² = {round(r2,4)}')
plt.legend()
plt.show()

# Previsão do valor de X0 para L = 165
L_pred = 165
X_pred = m * L_pred + b
print(f"L = {L_pred} --> X = {round(X_pred, 3)}")
