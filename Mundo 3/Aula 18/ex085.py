num = [[],[]]
valor = 0
for c in range (1, 8):
    valor = int(input('Digite um valor: '))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('_-_-'*30)
num[0].sort()
num[1].sorte()
print(f'Os valores pares digiados foram: {num[0]}')
print(f'Os valores impares digitados foran: {num[1]}')
