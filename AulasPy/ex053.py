med = 0
midade = 0
MulheresMenor = 0
inome = ''
for c in range(0, 4):
    nome = input('Nome de uma pessoa: ')
    idade = int(input('Idade dessa pessoa: '))
    sexo = input('Sexo M ou F? ').upper()
    if idade > midade and sexo == 'M':
        midade = idade
        inome = nome
    med += idade
    if sexo == 'F' and idade < 20:
        MulheresMenor += 1
    print('='* 30)
print(med / 4)
print('O homem mais velho se chama {} e tem {} anos'.format(inome, midade))
print('Nesse grupo tem {} mulheres menor de idade'.format(MulheresMenor))

