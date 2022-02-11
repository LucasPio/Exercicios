pa = int(input('Escreva o início da PA: '))
r = int(input('Qual a razão dessa PA? '))
s = 0
for c in range(0,10):
    if c == 0:
        print('os 10 primeiros termos dessa PA são:'
            '{}'.format(pa))
    elif c == 1:
        s = pa + r
        print('os 10 primeiros termos dessa PA são:'
              '{}'.format(s))
    else:
        s += r
        print('os 10 primeiros termos dessa PA são:'
              '{}'.format(s))

