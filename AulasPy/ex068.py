nt50 = nt1 = nt20 = nt10 = 0
saque = int(input('Valor a ser sacado (apenas valores inteiros)'))
while saque > 0:
    if saque >= 50:
        nt50 += 1
        saque -= 50
    elif saque >= 20:
        nt20 += 1
        saque -= 20
    elif saque >= 10:
        nt10 += 1
        saque -= 10
    else:
        nt1 += 1
        saque -= 1
print('='*15)
print(f'total de {nt50} celulas de R$50')
print(f'total de {nt20} celulas de R$20')
print(f'Total de {nt10} celulas de R$10')
print(f'Total de {nt1} celulas de R$1')
print('='*15)