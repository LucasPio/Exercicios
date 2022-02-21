MaiorIdade = cont = MMenor = 0
while True:
    print('=-='*10)
    print('     Cadastro de pessoas')
    print('=-='*10)
    idade = int(input('Digite a idade de uma pessoa: '))

    if idade > 18:
        MaiorIdade += 1
    while True:
        sexo = input('Sexo [M/F]').upper()
        if sexo == "M":
            cont += 1
        if sexo == 'F' and idade < 20:
            MMenor += 1
        if sexo == 'M' or sexo == 'F':
            break
    while True:
        c = input('Deseja Continuar? ').upper()
        if c == 'S':
            break
        elif c == 'N':
            break
    if c == 'N':
        break
print(f'ao todo temos {MaiorIdade} pessoas maiores de idade')
print(f'dentre eles {cont} são homens')
print(f'e dentre essas pessoas {MMenor } são mulheres com menos de 20 anos')


