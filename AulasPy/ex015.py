import math
co = float(input('comprimento do cateto oposto'))
ca = float(input('comprimento do cateto adjacente'))
hi = math.hypot(co, ca)

print('A hipetenusa de {} e {} é {:.3f}'.format(co, ca, hi))