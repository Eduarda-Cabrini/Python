numeros = list()
while True:
    n = int (input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quem continuar? [s/n]'))
    if r in 'Nn':
        break
print('-_-_' * 30)
numeros.sort()
print(f'Você adicionou os valores {numeros}')