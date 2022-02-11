dias = int(input('por quantos dias você alugou o carro? '))
km = float(input('por quantos km você usou o carro '))
preço = km * 0.15 + dias * 60
print('o preço a pagar é de {:.2f}'.format(preço))