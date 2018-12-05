
print("**********************************")
print("*bem vindo ao jogo de adivinhação*")
print("**********************************")

numero_secreto = 42
chute = input("Digite um número: \n")
chute = int(chute)

print("Você digitou ", chute)

if(numero_secreto == chute):
    print("Você acertou")
else: 
    print("Você errou")