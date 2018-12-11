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
    if(chute > numero_secreto):
        print("Você errou, o seu chute foi maior que o número secreto")
    elif(chute < numero_secreto):
        print("Você errou, o seu chute foi menor que o número secreto")