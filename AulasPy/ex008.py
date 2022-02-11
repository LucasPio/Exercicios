Real = float(input('quantos reais você tem na sua carteira? R$'))
Dolar = 5.26
Euro = 6.02
Btc = 228970.96

print('você pode comprar USD${:.2f} dolares\n'
      'ou você pode comprar €{:.2f} euros'.format((Real / Dolar),(Real / Euro)))
