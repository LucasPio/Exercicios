a = float(input('Digite um dos lados de um triangulo'))
b = float(input('Digite mais um lado do triangulo'))
c = float(input('Digite o último lado do triangulo'))
d = a<b+c
e = b<a+c
f = c<a+b
if  d == True and e == True and f == True:
    print('\033[7;30m sim é possivel fazer um triangulo com esses valores\033[m')
else:
    print('não é possivel fazer esse triangulo')

