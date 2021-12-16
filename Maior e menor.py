num1 = int(input("digite uma numero: "))

num2 = int(input("digite outra numero: "))

num3 = int(input("digite mais uma numero: "))


MaiorNumero = num1

if num2 > MaiorNumero:
    MaiorNumero = num2

if num3 > MaiorNumero:
    MaiorNumero = num3

    print("o maior número é", MaiorNumero)

else:
    print("o maior número é", MaiorNumero)

MenorNumero = num1

if num2 < num1:
    MenorNumero = num2

if num3 < num2:
    MenorNumero = num3

    print("o menor número é", MenorNumero)

else:
    print("o menor número é", MenorNumero)
