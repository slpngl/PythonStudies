print("")
print("*****************************")
print("Bem vindo ao jogo de adivinhação")
print("*****************************")

numero_secreto = 42
chute = input ("Digite seu número")

print("Você digitou" ,chute)

chutado = int(chute)

# Necessário fazer a conversão pois  o input vem com string

acertou = numero_secreto == chutado
maior = chutado > numero_secreto
menor = chutado < numero_secreto

if (acertou):
     print("Você acertou")
else:
    if(maior):
        print("você errou, o número secreto é mais baixo")
    elif(menor):
        print("você errou, o número secreto é mais alto")

print("FIM DO JOGO")
