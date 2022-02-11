count = 0
num = int(input('digite um número'))
for c in range (1, num+1):
    if num % c == 0:
        count += 1
        print('\033[1;33m', end="")
        print('{}'.format( c,  end=""))
    else:
        print('\033[1;31m', end="")
        print('{}'.format( c,  end=""))
if count == 2:
    print('\033[0;0;0messe número é primo, pois ele foi dividido {} vezes'.format(count),   end="")
else:
    print('esse número não é primo, pois foi dividido {} vezes'.format(count),   end="")
