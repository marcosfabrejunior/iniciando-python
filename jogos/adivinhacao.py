import random
import sys


def jogar():

    print("**********************************")
    print("*bem vindo ao jogo de adivinhação*")
    print("**********************************")


    numero_secreto = random.randrange(0,101)
    total_tentativas = 3
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) - Fácil | (2) - Médio | (3) - Difícil")

    nivel = int(input("Define o nível"))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    elif (nivel == 3):
        total_tentativas = 5
    else:
        print("Opção incorreta.")
        sys.exit()



    # função format()
    # print("R$ {:07.2f}".format(1.38))


    # while - início
    # while(rodada <= total_tentativas):
    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {0} de {1} ".format(rodada,total_tentativas))
        chute = input("Digite um número entre 1 e 100: \n")
        chute = int(chute)

        if (chute < 1 or chute > 100):
            print("Número fora da área de tentativas")
            continue

        print("Você digitou ", chute)

        if(numero_secreto == chute):
            print("Você acertou e fez {}".format(pontos))
            break
        else:  
            if(chute > numero_secreto):
                print("Você errou, o seu chute foi maior que o número secreto")
            elif(chute < numero_secreto):
                print("Você errou, o seu chute foi menor que o número secreto")
            
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")
            
    # while - fim

if(__name__ == "__main__"):
    jogar()