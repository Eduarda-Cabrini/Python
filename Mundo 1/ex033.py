a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado é {}: '.format(menor))
print('O maior valor digitado é {}: '.format(maior))