sair = ''
total = cont = totProd = MCaro = MBarato = 0
while True:
    produto = input('Qual o nome do produto comprado? ')
    preço = float(input('Qual o preço deste produto? '))
    cont +=1
    total += preço
    if cont == 1:
        MBarato = preço
    if preço > 1000:
        totProd += 1
    if MBarato > preço:
        MBarato = preço
    sair = input('Deseja continuar? [s/n]').upper()
    if sair == 'N':
        break
print('*'*6, 'Fim do programa', '*'*6)
print(f'O valor total da compra foi de {total:.2f}')
print(f'Temos {totProd} produtos custando mais de 1000 reais')
print(f'O produto mais barato custou {MBarato}')