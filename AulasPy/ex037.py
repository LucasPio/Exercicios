Nota1 = float(input('Digite sua nota '))
Nota2 = float(input('Digite outra nota '))
Nota3 = float(input('Digite mais uma nota'))
Nota4 = float(input('Digite outra nota'))

M = (Nota1+Nota2+Nota3+Nota4) / 4
if M < 5:
    print('A média deste aluno é {}'.format(M))
    print('ele foi Reprovado')
elif 5 <= M <= 6.9:
    print('A média deste aluno é {}'.format(M))
    print('ele ficou em Recuperação')
else:
    print('A média deste aluno é {}'. format(M))
    print('ele foi Aprovado')