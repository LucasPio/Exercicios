Num = int(input('\033[4;30;45mdigite um número inteiro\033[m'))
a = Num % 2
if a == 0:
    print('O número {} é par'.format(Num))
else:
    print('O número {} é impar'.format(Num))