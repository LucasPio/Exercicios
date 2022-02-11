import random
from time import sleep
Lista = ('Pedra', 'Papel', 'Tesoura')
num = ''

VitoriasU = 0
VitoriasR = 0
print('''
[1]Pedra
[2]Papel
[3]Tesoura
''')
while VitoriasU != 5 and VitoriasR != 5:
    User = int(input('Qual deseja escolher \n'))
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!')
    sleep(0.3)
    print('')

    num = random.randint(0, 2)
    if Lista[num] == 'Pedra' and User == 2:
        print('\033[1;33;40mVocê ganhou\033[m')
        VitoriasU += 1
        print('\033[1mVocê tem {} vitorias'.format(VitoriasU))
        print('\033[1mO robo tem {} vitorias'.format(VitoriasR))
    elif Lista[num] == 'Papel' and User == 3:
        print('\033[1;33;40mVocê ganhou\033[m')
        VitoriasU += 1
        print('\033[1mVocê tem {} vitorias\033[m'.format(VitoriasU))
        print('\033[1mO robo tem {} vitorias\033[m'.format(VitoriasR))
    elif Lista[num] == 'Tesoura' and User == 1:
        print('\033[1;33;40mVocê ganhou\033[m')
        VitoriasU += 1
        print('\033[1mVocê tem {} vitorias\033[m'.format(VitoriasU))
        print('\033[1mO robo tem {} vitorias\033[m'.format(VitoriasR))
    elif num == User:
        print('Empate')
        print('\033[1mVocê tem {} vitorias\033[m'.format(VitoriasU))
        print('\033[1mO robo tem {} vitorias\033[m'.format(VitoriasR))
    else:
        print('\033[1;33;40m Você perdeu \033[m ')
        VitoriasR += 1
        print('\033[1mVocê tem {} vitorias\033[m'.format(VitoriasU))
        print('\033[1mO robo tem {} vitorias\033[m'.format(VitoriasR))
    print('')
    print('Você escolheu', Lista[User - 1])
    print('O computador escolheu', Lista[num])
if VitoriasU == 5:
    print('\033[1;40mParabéns, você ganhou a partida\033[m')
else:
    print('\033[1;40mVocê perdeu, mais sorte na próxima\033[m')