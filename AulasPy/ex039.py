a = float(input('Digite um dos lados de um triangulo'))
b = float(input('Digite mais um lado do triangulo'))
c = float(input('Digite o último lado do triangulo'))
d = a < b + c
e = b < a + c
f = c < a + b
if  d == True and e == True and f == True:
    print('\033[1;30;45m sim é possivel formar um triangulo com esses valores\033[m')
    if a == b and b == c:
        print('poderá formar um triangulo Equilátero')
    elif a == b or b == c or c == a:
        print('Poderá formar um triangulo Isósceles')
    else:
        print('Poderá formar um triangulo Escaleno')
else:

    print('não é possivel fazer esse triangulo')