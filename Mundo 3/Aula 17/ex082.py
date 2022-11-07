num = list ()
pares = list()
imp = list ()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar [s/n]? '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 ==0:
        pares.append(v)
    elif v % 2 == 1 :
        imp.append(v)
print('_-_-' * 30)
print(f'A lista completa é {num} ')
print(f'A lista dos pares é {pares} ')
print(f'A lista dos impares é {imp}')