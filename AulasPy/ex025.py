n = input('Digite seu nome completo ')
n = n.lower()
nome = n.split()
num = len(nome)
int(num)
print('Prazer em te conhecer!')
print('Seu primeiro nome é ', nome[0].capitalize())
print('Seu último nome é ', nome[num-1].capitalize())
