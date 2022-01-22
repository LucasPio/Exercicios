import random
a = random.randint(0, 100)

count = -1
while count <= 0:



    b = int(input("escolha um numero entre 0 e 100: "))


    if b > a:
            print("chute um valor menor")

    elif b < a:
            print("chute um valor maior")


    else:
            print("parabens você acertou", a)
            count = b == a
