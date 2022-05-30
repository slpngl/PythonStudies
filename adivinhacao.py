print("")
print("*****************************")
print("Bem vindo ao jogo de adivinhação")
print("*****************************")

numero_secreto = 42
chute = input ("Digite seu número")

print("Você digitou" ,chute)

chutado = int(chute)

# Necessário fazer a conversão pois  o input vem com string

if ( numero_secreto == chutado ):
     print("Você acertou")
else:
    print("você errou")

print("FIM DO JOGO")
