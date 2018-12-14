def jogar():
    print("**********************************")
    print("*bem vindo ao jogo de forca*")
    print("**********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    palavra_secreta = palavra_secreta.lower()

    while (not enforcou and not acertou):
        chute = input("Qual Letra?")
        chute = chute.lower()
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                

            index = index + 1

        print("jogando...")


if(__name__ == "__main__"):
    jogar()