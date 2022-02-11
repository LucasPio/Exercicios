Sal = float(input('Salário do funcionario: '))

if Sal < 1250.00:
    print('O novo salário é de {}{:.2f}{} Reais'.format('\033[1;34m',Sal * 1.15,'\033[m'))
else:
    print('O novo salário é de {}{:.2f}{} Reais'.format('\033[1;34m',Sal * 1.10,'\033[m'))