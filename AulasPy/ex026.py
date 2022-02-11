from random import randint

NúmeroC = randint(0, 5)
NúmeroU = int(input('Digite um número inteiro entre 0 e 5: '))
if NúmeroU == NúmeroC:
    print('você é um cara de sorte, você acertou')
else:
    print('que azar você errou')