soma = 0
for c in range(1, 500):
    if c % 2 == 0:
        a = '1'
    else:
        if  c % 3 == 0:
            soma += c
            print(soma)