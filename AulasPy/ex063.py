s = contador = 0
while True:
    num = int(input('Digite um valor inteiro [Digite 999 para parar]'))
    if num == 999:
        break
    s += num
    contador += 1
print(f'A soma dos {contador} valores digitados foi {s}')
