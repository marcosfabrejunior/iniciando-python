
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
        chute = input("Qual Letra?")
        chute = chute.lower()
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
            
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)
    
    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")



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


if(__name__ == "__main__"):
    jogar()