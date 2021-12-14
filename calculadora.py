
num1= float(input("digite o primeiro numero: "))

num2= float(input("digite o segundo numero: "))

print("1-adicao")
print("2-subtracao")
print("3-multiplicacao")
print("4-divisao")

oper=int(input("escolha a operacao: "))

if oper == 1:
    num3=num1+num2
    print("A soma dos numeros é", num3)

elif oper == 2:
    num3=num1-num2
    print("A subtracao dos numeros é",num3)

elif oper == 3:
    num3=num1*num2
    print("A multiplicacao dos numeros é",num3)

elif oper == 4:
    num3=num1/num2
    print("A divisao dos numeros é",num3)

else:
    print("escolha um numero entre  1 e 4")


