casa = float(input('qual o valor da casa? '))
sal = float(input('Qual o seu salário? '))
Anos = int(input('Em quantos anos será pago?'))

Meses = Anos * 12
Val = sal * 0.30
preço = casa / Meses

if Val < preço:
    print('Você não pode financiar essa casa,\n'
          'Pois o valor mensal do financiamento é de {}\n'
          'e você ganha menos que o suficiente para paga-lo'.format(preço))
else:
    print('Parabéns sua casa foi financiada\n'
          'a um valor de {} reais por mês'.format(preço))