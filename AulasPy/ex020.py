nome = input('Qual seu Nome? ')
nomeM = nome.upper()
nomem = nome.lower()
nomeL = nome.replace(' ', '')
nome1 = nome.split()
print('o nome {} em letras maiusculas é {}'.format(nome, nomeM))
print('o nome {} em letras Minusculas é {}'.format(nome, nomem))
print('o nome {} possuí {} letras'.format(nome, len(nomeL)))
print('o primeiro nome possuí {} letras'.format(len(nome1[0])))
print(nome1)