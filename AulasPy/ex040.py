Altura = float(input('Qual sua altura: '))
Peso = float(input('Qual o seu peso: '))
IMC = Peso / Altura ** 2
print('{:.2f} IMC'.format(IMC))
if IMC <= 18.5:
    print('Abaixo do peso')
elif 18.5 < IMC <= 25:
    print('Peso ideal')
elif 25 < IMC <= 30:
    print('Sobrepeso')
elif 30 < IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')