S = 0
for c in range(1,7):
    Num = int(input('Digite o {} valor'.format(c)))
    if Num % 2 == 0:
        S += Num
print(S)