num1 = float(input('Digite um valor '))
num2 = float(input('Mais um Valor '))
if num1 > num2:
    print('{} é o maior'.format(num1))
elif num2 > num1:
    print('{} é o maior'.format(num2))
else:
    print('os números {} e {} são iguais'.format(num1, num2))
