Produto = float(input('Preço do produto: '))
Método = input('Forma de Pagamento: ')
QuantasVezes = int(input('Quantas Vezes será pago?' ))
Método = Método.lower()
if Método == 'dinheiro' and QuantasVezes == 1 or Método == 'cheque' and QuantasVezes == 1:
    Preço = Produto * 0.90
    print('Você tem 10% de desconto nesse produto que custará {:.2f}'.format(Preço))
elif Método == 'cartão' and QuantasVezes == 1:
    Preço = Produto * 0.95
    print('Você tem 5% de desconto nesse produto que custará {:.2f}'.format(Preço))
elif Método == 'cartão' and QuantasVezes == 2:
    Preço = Produto
    print('Você pagará o preço normal do produto que é {:.2f}'.format(Preço))
elif Método == 'cartão' and QuantasVezes >= 3:
    Preço = Produto * 1.20
    print('Você irá pagar {:.2f} com o Juros'.format(Preço))
