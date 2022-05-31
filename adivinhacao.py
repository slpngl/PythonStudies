print("")
print("*****************************")
print("Bem vindo ao jogo de adivinhação")
print("*****************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Essa é sua", rodada, "rodada")

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # String interpolation

    chute = input("Digite seu número")

    print("Você digitou", chute)

    chutado = int(chute)

    # Necessário fazer a conversão pois  o input vem com string

    acertou = numero_secreto == chutado
    maior = chutado > numero_secreto
    menor = chutado < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if (maior):
            print("você errou, o número secreto é mais baixo")
        elif (menor):
            print("você errou, o número secreto é mais alto")

    rodada = rodada + 1

print("FIM DO JOGO")
