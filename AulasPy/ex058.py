'''num = int(input('Digite um valor'))
cont = 0
fat = 1
while cont != num:
    print(cont)
    fat += fat * cont
    cont += 1
print(fat)'''
num = int(input('Digite um valor'))
fat = 1
for c in range(1, num):
    fat += fat * c
print('o Fatorial de {} é {}'.format(num, fat))