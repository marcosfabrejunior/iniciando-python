import sys

# 2) Um sapateiro faz 6 sapatos por hora, se fizer somente sapatos, e 5 cintos por hora, se fizer 
# somente cintos. Ele gasta 2 unidades de couro para fabricar 1 unidade de sapato e 1 unidade de couro 
# para fabricar uma unidade de cinto. Sabendo-se que o total disponível de couro é de 6 unidades e que o 
# lucro unitário por sapato é de 5 unidades monetárias e o do cinto é de 2 unidades monetárias,
#  pede-se: o modelo do sistema de produção do sapateiro, se o objetivo é maximizar seu lucro por hora.

# Resolução
# ---------------------------------------------------------------
# Objetivo -> 5x1 + 2x2


# Restrições
# 10x1 + 12x2 <= 60 min
# 2x1 + x2 <= 6
# ---------------------------------------------------------------

# Restrições
def restricoes(a,b):
    return ((10*a + 12*b) <= 60) and ((2*a + b) <= 6) and (a >= 0) and b >= 0


# Função objetivo
def lucro_max(coef,x, count):
    lucro_max = 0
    for i in range(count):
        lucro_max = lucro_max + (coef[i]*x[i])
    
    return lucro_max


def maximiza_lucro():

    # quantidade de grandezas. Ex. X1 X2 X3
    count = 2

    # coeficientes respectivos que acompanham as grandezas
    coeficientes = [5,2]
    

    # Atribuições do modelo
    
    x = []
    for k in count - 1:
        x.append(0)

    coef = []
    for l in count - 1:
        coef.append(coeficientes[l])

    # Atribuições da resolução
    max = []
    for m in count - 1:
         max.append(0)

    lc_options = []
    lc_max = []

    # descobre o valor máximo de cada coeficiente
    for i in range(count):
        while restricoes(x[0], x[1]): # tornar isso generico x[n]
            x[i] = x[i] + 1  
            max[i] = x[i]
        x[i] = 0

    maior_lucro = 0
    valores = ""
    for a in range(max[0]):
        for b in range(max[1]):
            if(restricoes(a, b)):
                x[0] = a
                x[1] = b
                if(lucro_max(coef,x, count) > maior_lucro):
                    maior_lucro = lucro_max(coef,x, count)
                    valores = [a,b]
    
    print(maior_lucro)
    return valores

# precisa fazer uma função recursiva
def solver():
    pass
    
print(maximiza_lucro())
