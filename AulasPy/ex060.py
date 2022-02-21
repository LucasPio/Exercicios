fim = int(input('Digite o fim da sequência'))
i= 1
n1 = 0
n2 = 1
contador = 0
while contador < fim:
    contador += 1
    if contador == 1:
        print(n1, n2, end=' ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=' ')
