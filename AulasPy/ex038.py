from datetime import date
nasc = int(input('Digite seu Ano de nascimento: '))
Ano = date.today().year
Idade = Ano - nasc
if nasc < Ano:
    if Idade <= 9:
        print('Classificação: Mirim')
        print('O atleta tem {} anos'.format(Idade))
    elif Idade <= 14:
        print('Classificação: Infantil')
        print('O atleta tem {} anos'.format(Idade))
    elif Idade <= 19:
        print('Classificação: Junior')
        print('O atleta tem {} anos'.format(Idade))
    elif Idade <= 25:
        print('Classificação: Senior')
        print('O atleta tem {} anos'.format(Idade))
    else:
        print('Classificação: Master')
        print('O atleta tem {} anos'.format(Idade))