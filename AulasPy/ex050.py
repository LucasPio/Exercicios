frase = input('Digite uma frase').lower()
frase = frase.replace(' ', '')
txt = frase[::-1]
print('A frase normal é: ', frase)
print('A frase invertida é igual a: ', txt)
if frase == txt:
    print('está frase é um palíndromo')
else:
    print('está é uma frase')
