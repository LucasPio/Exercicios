cont = 0
num = (int(input('Digite um valor')), int(input('Digite outro valor')), int(input('digite mais um valor')),
       int(input('Digite um último valor')))
for n in num:
    if n == 9:
        cont += 1
print(cont)
if 3 in num:
    print('O primeiro 3 aparece na {}° posição'.format(num.index(3)+1))
for p in num:
    if p % 2 == 0:
        print(p, end=' ')