import matplotlib.pyplot as plt
import numpy as np

def lin_reg(x,y):  #função da regressão linear
    assert len(x) == len(y)  #garante que os vetores têm o mesmo tamanho
    assert len(x)>=3   #garante que o tamanho da primeira lista é maior ou igual a 3
    
    #cálculos dos somatórios
    sum_xy_i = np.sum(x*y)
    sum_x_i = np.sum(x)
    sum_y_i = np.sum(y)
    sum_x2_i = np.sum(x**2)
    sum_y2_i = np.sum(y**2)
    
    #fórmulas da regressão linear
    m = (len(x) * sum_xy_i - sum_x_i*sum_y_i) / (len(x)*sum_x2_i - (sum_x_i)**2)
    b = (sum_x2_i*sum_y_i - sum_x_i*sum_xy_i) / (len(x)*sum_x2_i - (sum_x_i)**2)
    #coeficiente de determinação (avalia a qualidade do ajuste    1 == ajuste perfeito)
    r = (len(x) * sum_xy_i - sum_x_i*sum_y_i)**2 / ((len(x)*sum_x2_i - (sum_x_i)**2) * (len(x)*sum_y2_i - (sum_y_i)**2))
    
    #incertezas
    delta_m = np.abs(m) * np.sqrt(((1/r) - 1) / len(x) - 2)
    delta_b = delta_m * np.sqrt( sum_x2_i / len(x) )
    
    return m, b, r, delta_m, delta_b
    
    
# Dados de exemplo
L = np.array([222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0]) # for X
X = np.array([2.3  , 2.2  , 2.0  , 1.8  , 1.6  , 1.4  , 1.2  , 1.0 ]) # for Y


plt.plot(L, X , 'r.')
plt.xlabel('L (cm)')
plt.ylabel('X (cm)')
#limites dos eixos
ax = min(L)*1.1
bx = max(L)*1.1
cy = min(X)*1.1
dy = max(X)*1.1
plt.xlim(ax, bx)
plt.ylim(cy, dy)

#geração da linha de regressão
x = np.linspace(ax, bx,100)  #100 valores entre os limites do eixo x
m, b, r, delta_m, delta_b = lin_reg(L,X)
y = m*x + b

plt.plot(x, y, '-g', label='y=2x+1', linewidth=1)
plt.title("m = "+str(round(m,5))+" ; b = "+str(round(b,5))+" ; r² = "+str(round(r,5)))
plt.show()

#Calcula e exibe o valor de X correspondente a L = 165 cm usando a equação da reta.
print("L = 165 --> X = "+str(round(m*165+b,3)))