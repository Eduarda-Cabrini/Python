n1 = float(input('Digite o 1 valor: '))
n2 = float(input('Digite o 2 valor: '))
finalizar = False
while not finalizar:
    menu = int(input('''Agora, insira o número que corresponde ao que você quer fazer com seus valores
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA:    '''))
    soma = n1 + n2
    mult = n1 * n2
    maiorvalor = ''
    if menu == 1:
        print('A soma dos valores é de {}.'.format(soma))
    if menu == 2:
        print('A multiplicação entre os valores é de {}.'.format(mult))
    if menu == 3:
        if n1 > n2:
            maiorvalor = n1
            print('O maior valor entre os dois inseridos é de {}.'.format(maiorvalor))
        if n2 > n1:
            maiorvalor = n2
            print('O maior valor entre os dois inseridos é de {}.'.format(maiorvalor))
        if n2 == n1:
            print('Os dois valores são iguais!')
    if menu == 4:
        print('Seu desejo é uma ordem!')
        n1 = int(input('Insira o novo 1 valor: '))
        n2 = int(input('Insira o novo 2 valor: '))
    if menu == 5:
        print('Entendido, estamos finalizando o programa! Tchauzinho! :)')
        finalizar = True
    print('-='*10)