temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(str(input('Peso: ')))
    if len(princ) == 0:
         mai = men = temp[1]
    else :
        if temp [1] > mai:
            mai = temp[1]
        if temp [1] < men:
            men = temp [1]
    princ.append(temp [:])
    temp.clear()
    resp = str(input('Quer continuar [s/n]? '))
    if resp in 'Nn' :
        break
print('_-_-' * 30)
print(f'Está cadastrado {len(princ)} pessoas.  ')
print(f'O maior peso foi de {mai}kg peso de', end='' )
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men}kg, Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()