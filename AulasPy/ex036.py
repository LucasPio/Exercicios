from datetime import date
Ano = int(input('Coloque seu ano de nascimento'))
AnoAtual = date.today().year
alistamento = AnoAtual - Ano
if Ano > AnoAtual:
    print('coloque uma data válida')
else:
    print('Quem nasceu em {} tem {} e deve se alistar em {}'.format(Ano, alistamento, Ano + 18))
    if alistamento == 18:
        print('você já pode se alistar ')
    elif alistamento > 18:
        print('Você já deveria ter se alistado a {} anos '.format(alistamento - 18))
    else:
        print('Você não pode se alistar ainda faltam {} anos '.format(alistamento))
        print('Você deverá se alistar em {}'.format(AnoAtual + alistamento))
