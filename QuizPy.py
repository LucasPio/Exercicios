

print("quanto é 6+4 ")
print("1 - 12")
print("2 - 10")
print("3 - 12")
Q1 = int(input("4 - 8"))

print("animais que comem carne sao? ")
print("1 - carnivoros")
print("2 - herbivoros")
print("3 - predadores")
Q2 = int(input("4 - presas"))

print("Na natureza nada se ...., nada se perde, tudo se transforma. Complete a frase ")
print("1 - tira")
print("2 - muda")
print("3 - transforma")
Q3 = int(input("4 - cria"))

print("quantas operacoes basicas possui a matematica")
print("1 - 4")
print("2 - 8")
print("3 - 12")
Q4 = int(input("4 - 18"))

pontos = 0
if Q1 == 2:
    pontos += 1
    print(Q1)
else:
    print("voce errou")
if Q2 == 1:
    pontos += 1
    print(Q2)
else:
    print("voce errou")
if Q3 == 4:
    pontos += 1
    print(Q3)
else:
    print("voce errou")
if Q4 == 1:
    pontos += 1
    print(Q4)
else:
    print("voce errou")
print("você acertou", pontos, "de 4 questões")