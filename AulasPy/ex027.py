Vel = int(input('Digite a Velocidade do carro '))
multa = (Vel - 80) * 7
if Vel < 80:
    print('normal')
else:
    print('você recebeu uma multa de {:.2f}'.format(multa))