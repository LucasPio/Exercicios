num = int(input('Digite um número inteiro'))
print('''Qual Conversão deseja fazer
[1]Binário
[2]Octal
[3]Hexadecimal''')
Conv = int(input(''))
if Conv == 1:
    print('o Valor {} em Binário é igual a {}'.format(num, bin(num)[2:]))
elif Conv == 2:
    print('O valor Octal de {} é igual a {}'.format(num, oct(num)[2:]))
elif Conv == 3:
    print('O valor Hexadecimal de {} é igual a {}'.format(num, hex(num)[2:]))