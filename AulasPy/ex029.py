Viagem = int(input('Qual a distancia da viagem? '))
if Viagem < 200:
    print('A viagem ira custar \033[1;35;40m{}\033[m reais'.format(Viagem * 0.50))
else:
    print('A viagem irá custar {} reais'.format(Viagem * 0.45))