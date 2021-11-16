número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
  print('O número foi {} é par'.format(resultado))
else:
    print('O número {} é impar'.format(resultado))