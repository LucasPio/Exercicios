largura = float(input('coloque a largura de uma parede'))
altura = float(input('coloque a altura de uma parede'))
metros = largura * altura
QTinta = metros / 2
print('a área dessa parede é de {:.3f}m² \n'
      'a quantidade de litros de tinta necessária é {:.3f}'.format((largura * altura), QTinta))