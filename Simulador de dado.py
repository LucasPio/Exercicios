import random



dado = random.randint(1, 6)
GirarDado = (input("você gostaria de girar novamente o dado?"))
print(dado)
if GirarDado == "sim":
    dado = random.randint(1, 6)
    print(dado)

elif GirarDado == "nao":
    print(dado)

elif GirarDado == "n":
    print(dado)

elif GirarDado == "s":
    dado = random.randint(1, 6)
    print(dado)

else:
    print("coloque sim ou nao")


