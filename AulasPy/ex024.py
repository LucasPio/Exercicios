frase = input('digite uma frase')
frase = frase.lower()
frase = frase.strip()
a = frase.count('a')
a = a -2
print('a Letra A apareceu {} vezes'.format(a) )
print ('A letra A apareceu pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra A apareceu pela última vez na posição {}'.format(frase.rfind('a')+1))
