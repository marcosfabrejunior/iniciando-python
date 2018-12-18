def jogar():
    print("**********************************")
    print("*bem vindo ao jogo de forca*")
    print("**********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    letras_acertadas = ["_" for letra in palavra_secreta]
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
        acertou = "_" in letras_acertadas
        
        print(letras_acertadas)
    
    if(acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")


if(__name__ == "__main__"):
    jogar()