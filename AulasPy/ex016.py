from math import radians, sin, cos,tan
angulo = float(input('digite um angulo'))
seno = sin(radians(angulo))
print('o angulo {} tem o Seno de {:.2f}'.format(angulo, seno))
cos = cos(radians(angulo))
print('o angulo {} tem o Cosseno de {:.2f}'.format(angulo, cos))
tan = tan(radians(angulo))
print('o angulo {} tem a Tangente de {:.2f}'.format(angulo, tan))