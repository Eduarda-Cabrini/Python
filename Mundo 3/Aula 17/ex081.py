valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [s/n] '))
    if resp in 'Nn' :
        break
print('-_-_' * 30)
print (f'Você digitou {len(valores)} elementos. ')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 está dentro da lista...')
else:
    print('O valor 5 não está na lista...')

