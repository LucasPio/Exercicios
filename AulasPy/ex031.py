num1 = int(input('Digite um número'))
num2 = int(input('Digite outro número'))
num3 = int(input('Digite mais um número'))

if num1 > num2:
    maior = num1
if num2 > num1:
   maior = num2
if num3 > num2:
    if num3 > num1:
        maior = num3
if num1 < num2:
    menor = num1
if num2 < num3:
    if num1 > num2:
        menor = num2
if num3 < num1:
    if num2 > num3:
        menor = num3
print('maior valor é', '\033[1;34m', maior,'\033[m')
print('menor valor é', '\033[1;34m', menor,'\033[m')
