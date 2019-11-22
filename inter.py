import numpy as np

dias = [1,2,3,4,7,8,9,10,11,14,15,16,17,18,21,22,23,24,25,28,29,30,31]
dol = [4.1740 , 4.1546,4.1012,4.0610,4.0688,4.0868,4.0954,4.1145,4.1060,4.1263,4.1488,4.1714,4.1457,4.1376,4.1319,4.0858,4.0721,4.0089,4.0133,3.9793,3.9946,4.0186,4.0041]

tam = len(dias)

coeficientes = []
dados = []

for n in range(tam):

    for k in range(n+1,tam):
        
        if(n+1 > tam):
            break
        # operacao com inversa de matriz para obter a resolucao do sistema de equacoes
        A = np.array([[dias[n], 1], [dias[k], 1]])
        B = np.array([dol[n], dol[k]])
        X = np.linalg.inv(A).dot(B)

        print("PAR -> (%d, %f) , (%d, %f)" %(dias[n], dol[n], dias[k], dol[k]))

        # adiciona os dados das duas funcoes, que foram usadas para encontrar os coeficiente (m,b)
        # mantendo uma referência entre os index's
        dados.append([ ( dias[n], dol[n]) ,  (dias[k], dol[k] ) ])
        coeficientes.append(X)
        # print( X)


# o minimo é um valor muito grande inicialmente, para que qualquer valor seja menor que o inicial
minimo = 1212133123123131313232
index = 0
for i in range(len(coeficientes)):
    soma = 0
    for n in range(tam):
        # soma os módulos de cada função com os valores de (m,b) encontrados na iteração anterior
        soma += abs(dias[n]*coeficientes[i][0] + coeficientes[i][1] - dol[n])
    
    #verifica se a soma atual é a mínima
    if(soma < minimo):
        minimo = soma

        #obtem o número da interação atual, para recuperar os dados dos coeficientes
        index = i

print("O valor mínimo:", minimo)
print("(m,b) =>", coeficientes[index])
print("Dados: (dia, dólar)", dados[index])
