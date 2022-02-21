while True:
    contador = 0
    num = int(input('Deseja a tabuada de qual valor?'))
    if num < 0:
        break
    for contador in range(1, 11, 1):
        tab = num * contador
        print(f'{num}*{contador}={tab}')
