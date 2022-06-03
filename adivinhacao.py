import random

print("")
print("*****************************")
print("Bem vindo ao jogo de adivinhação")
print("*****************************")

#numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
rodada = 1

# while (rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):  # +1 pq o último número do range é excludente . então no caso seria algo como
    # menor que - 1 até menor que total de tentativas.

    print("Essa é sua", rodada, "rodada")

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # String interpolation

    chute = input("Digite um número entre 1 e 100")

    chutado = int(chute) # Necessário fazer a conversão pois  o input vem com string

    print("Você digitou", chutado)

    if (chutado < 1 or chutado > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chutado
    maior = chutado > numero_secreto
    menor = chutado < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if (maior):
            print("você errou, o número secreto é mais baixo")
        elif (menor):
            print("você errou, o número secreto é mais alto")

    rodada = rodada + 1

print("O número secreto é : {}".format(numero_secreto))
print("FIM DO JOGO")





