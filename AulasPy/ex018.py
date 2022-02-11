import random
n1 = input('primeiro aluno')
n2 = input('segundo aluno')
n3 = input('tereceiro aluno')
n4 = input('quarto aluno')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('a ordem de apresentação será\n {}'.format(lista))