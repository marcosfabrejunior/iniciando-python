
import random

def jogar():

    imprime_mensagem_abertura()
    
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    
    enforcou = False
    acertou = False



    
    erros = 0

    palavra_secreta = palavra_secreta.lower()

    while (not enforcou and not acertou):

        chute = pede_chute()


        

        if(chute in palavra_secreta):
            
            letras_acertadas = marca_chute_acertado(letras_acertadas, palavra_secreta, chute)
            
        else:
            erros += 1
            mostra_forca(erros)

        enforcou = erros == 8
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)
    
    if(acertou):
        print("Você ganhou")
        imprime_mensagem_venceu()
    else:
        imprime_mensagem_perdeu(palavra_secreta)



def imprime_mensagem_abertura():
    print("**********************************")
    print("*bem vindo ao jogo de forca      *")
    print("**********************************") 

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_palavras = []
    for linha in arquivo:
        lista_palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0,len(lista_palavras))

    palavra_secreta = lista_palavras[numero]
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute = input("Qual Letra?")
    chute = chute.lower()
    chute = chute.strip()
    return chute

def marca_chute_acertado(letras_acertadas, palavra_secreta, chute):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas

def imprime_mensagem_venceu():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mostra_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



if(__name__ == "__main__"):
    jogar()