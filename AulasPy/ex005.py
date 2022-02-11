import math
from math import (ceil)
nota1 = float(input('coloque a sua nota: '))
nota2 = float(input('coloque outra nota: '))
s = (nota1 + nota2) / 2
méd = math.ceil(s)
print('sua média final de {:.1f} e {:.1f} é {:.1f}'.format( nota1, nota2, méd))

