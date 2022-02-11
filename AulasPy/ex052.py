
count = 0
mpeso = 0
for c in range(0, 5):
    count += 1
    peso2 = float(input('Peso da {} pessoa'.format(count)))
    if count == 1:
        mepeso = peso2
    if  peso2 > mpeso:
        mpeso = peso2
    if peso2 < mepeso:
        mepeso = peso2
print('O maior peso é {}'.format(mpeso))
print('O menor peso é {}'.format(mepeso))

