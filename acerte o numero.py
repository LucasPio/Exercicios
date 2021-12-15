import random

a=random.randint(0,  10)
b= int(input("escolha um numero entre 0 e 10: "))



if b == a:
    print("você acertou, o numero era", a)


else:
    print("não foi dessa vez, o numero era", a)
    count = -1
    while (count <= 0):


        a = random.randint(0, 10)

        b = int(input("escolha um numero entre 0 e 10: "))

        count = b == a
        if b == a:
            print("você acertou, o numero era", a)


        else:
            print("não foi dessa vez, o numero era", a)

