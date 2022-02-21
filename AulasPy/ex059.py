paI = int(input('Escreva o início da PA: '))
calc = 10
contador = 0
pa = paI
r = int(input('Qual a razão dessa PA? '))
fim = pa + calc * r
resultado = []
pa = pa - r
parar = False
print('A progressão aritimética de {} e razão {} '.format(paI, r,))
print('tem os 10 primeiros valores: ', end=' ')
while not parar:
    while not contador == calc:
        termos = 10
        pa += r
        contador += 1
        print('→ {}'.format(pa), end=' ')
    print('')
    while calc != 0:
        calc = int(input('\npretende fazer mais quantos termos?'))
        pa += -2
        termos += calc
        if calc == 0:
            parar = True
            print('A quantidade de termos mostrados é igual a {}'.format(termos))
        contador = 0
        while  contador != calc:
            pa += r
            contador += 1
            print('→ {}'.format(pa), end=' ')

