num = int(input('digite um número inteiro'))
print('a tabuada de', num, 'é')
for c in range(0,11):
    s = num * c
    print('{} * {} =  {}'.format(num, c, s))