import matplotlib.pyplot as plt
import numpy as np

#velocidade contsante a uma distância de 10km
#medições == primeiros 9 minutos

X = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329]) #distância percorrida nos instantes contabilizados
T = np.array([0.00, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00]) #tempo

plt.plot(X, T, 's', color="purple", label='Pontos experimentais')  #o ciclista consegue manter uma velocidade constante caso se verifique que o gráfico dos dados é linear 
plt.xlabel('X (km)')
plt.ylabel('T (min)')
plt.show()

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


m, b, r, delta_m, delta_b = lin_reg(X, T)  #importante chamar a função antes de printar a variável r
print("R**2 = ", r)  #o r**2 é bastante próximo de 1 o que indica que a reta de regressão liner é bastante boa

#velocidade média
dist_total = X[-1] - X[0]  
tempo_total = T[-1] - T[0]  
v_media_km_min = dist_total / tempo_total  
v_media_km_h = v_media_km_min * 60  
 


