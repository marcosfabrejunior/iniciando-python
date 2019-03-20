import sys

# Uma empresa fabrica dois tipos de brinquedos B1 e B2 que utilizam recursos plásticos(até 1000 quilos estão disponíveis) 
# e horas de produção(até 40 horas estão disponíveis)

# O departamento de marketing colocou algumas restrições:

# Não fabricar mais de 700 dúzias do total de brinquedos, o número de dúzias fabricadas de B1 não deve exceder em 350 o 
# número de dúzias de B2

# A manufatura passou as seguintes informações: 
	
# Cada dúzia do brinquedo usa dois quilos de plástico e 3 minutos para a fabricação e cada dúzia do brinquedo B2 utiliza 
# 1 quilo de plástico e 4 minutos para serem feitos.

# A empresa deseja determinar qual a quantidade a ser produzida de cada produto de modo a maximizar o lucro total semanal

# 	O lucro estimado de B1 é $8,00/duzia e de B2 é de $5,00/dúzia

# Resolução
# ---------------------------------------------------------------
# x1 -> quantidade em duzias de B1
# x2 -> quantidade em dúzias de B2

# MAX 8x1 + 5x2

# restrições
# 2x1 + x2 <= 1000
# 3x1 + 4x2 <= 2400
# x1 + x2 <= 700
# x1 -x2 <= 350
# ---------------------------------------------------------------

# Restrições
def restricoes(a,b):
    return (((2*a) + b) <= 1000) and ((3*a + 4*b) <= 2400) and ((a + b) <= 700) and ((a-b) <= 350) and (a >= 0) and b >= 0


# Função objetivo
def lucro_max(coef,x, count):
    lucro_max = 0
    for i in range(count):
        lucro_max = lucro_max + (coef[i]*x[i])
    
    return lucro_max


def maximiza_lucro():

    # Atribuições do modelo
    count = 2
    x = []
    x.append(0)
    x.append(0)

    coef = []
    coef.append(8)
    coef.append(5)

    # Atribuições da resolução
    max = []
    max.append(0)
    max.append(0)

    lc_options = []
    lc_max = []

    # descobre o valor máximo de cada coeficiente
    for i in range(count):
        while restricoes(x[0], x[1]):
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
    
    return valores


print(maximiza_lucro())
