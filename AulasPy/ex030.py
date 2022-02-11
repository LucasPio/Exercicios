Ano = int(input('Digite um ano'))
if Ano % 4 == 0:
    print('\033[0;;44m esse é um ano bissexto \033[m')
else:
    print('esse é um ano normal')