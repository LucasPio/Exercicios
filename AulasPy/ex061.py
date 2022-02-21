soma = valores = num = 0    
while num != 999:
    num = int(input('Digite um número [Digite 999 para parar]'))
    if num != 999:
        valores += 1
        soma += num
print('os números digitados correspondem a soma de {} '.format(soma))
print('Foram digitados {} valores'.format(valores))

