def jogar():
    print("")
    print("*****************************")
    print("Bem vindo ao jogo da forca")
    print("*****************************")

    palavra_secreta = "secreta"
    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 1
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
                index = index + 1

        print("Jogando...")

        print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()

    #função principal.