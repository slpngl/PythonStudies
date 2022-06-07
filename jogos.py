import forca
import adivinhacao

def escolher_jogo():
    print("")
    print("*****************************")
    print("Bem vindo ao playroom")
    print("*****************************")

    print("Qual jogo deseja jogar?")
    print("(1) Advinhação - (2) Forca - ")

    jogo_strg = input("Defina o jogo escolido:")
    jogo = int(jogo_strg)

    if (jogo == 1):
        print("Advinhação")
        adivinhacao.jogar()

    elif (jogo == 2):
        print("forca")
        forca.jogar()

if (__name__ == "__main__"):
    escolher_jogo()
