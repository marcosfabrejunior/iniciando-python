import sys

# Restrições - Início


def rest_mao_obra(x_a, x_b, x_c):
    return ((7*x_a) + (3*x_b) + (3*x_c)) <= 150

def rest_material(x_a, x_b, x_c):
    return ((4*x_a) + (4*x_b) + (5*x_c)) <= 200

def nao_negatividade(x_a, x_b, x_c):
    return ((x_a) >= 0) and ((x_b) >= 0) and ((x_c) >= 0)
# Restrições - Fim

# Função objetivo
def lucro_max(coef,x, count):
    lucro_max = 0
    for i in range(count):
        lucro_max = lucro_max + (coef[i]*x[i])
    
    return lucro_max


def maximiza_lucro():

    # Atribuições do modelo
    count = 3
    x = []
    x.append(0)
    x.append(0)
    x.append(0)

    coef = []
    coef.append(4)
    coef.append(2)
    coef.append(3)

    # Atribuições da resolução
    max = []
    max.append(0)
    max.append(0)
    max.append(0)

    lc_options = []
    lc_max = []

    # descobre o valor máximo de cada coeficiente
    for i in range(count):
        while rest_mao_obra(x[0], x[1], x[2]) and rest_material(x[0], x[1], x[2]):
            x[i] = x[i] + 1  
            max[i] = x[i]
        x[i] = 0

    maior_lucro = 0
    valores = ""
    for a in range(max[0]):
        for b in range(max[1]):
            for c in range(max[2]):
                if(rest_mao_obra(a, b, c) and rest_material(a, b, c)):
                    x[0] = a
                    x[1] = b
                    x[2] = c
                    if(lucro_max(coef,x, count) > maior_lucro):
                        maior_lucro = lucro_max(coef,x, count)
                        valores = [a,b,c]
    
    return valores


print(maximiza_lucro())