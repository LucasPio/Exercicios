from random import randint
vit = 0
par = False
while True:
    numU = int(input('digite um valor'))
    numM = randint(1, 10)
    PI = input('Par ou Impar [p/i]')
    s = numU + numM
    if s % 2 == 0:
        r = 'Par'
    else:
        r = 'Impar'
    if s % 2 == 0:
        par = True
    else:
        par = False
    if PI == 'p' and par == True:
        print('Você venceu!!')
        v = 'Você'
        vit += 1
    elif PI == 'i' and par == False:
        print('Você venceu')
        v = 'Você'
        vit += 1
    else:
        print('Você perdeu')
        v = 'Computador'
    print(f'O computador escolheu {numM} e você escolheu {numU} então como {s} é {r} o vencedor é {v}')
    if v == 'Computador':
        break
print(f'O número total de vitorias foi {vit}')
