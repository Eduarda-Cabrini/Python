from random import randint
n = nc = cont = 0
e = ''
while True:
    n = int(input(f'Digite o seu valor: '))
    nc = randint(1, 11)
    s = n + nc
    e = str(input(f'Par ou ímpar [P/I]? ')).strip().upper()[0]
    while e not in 'PI':
        e = str(input(f'Par ou ímpar [P/I]? ')).strip().upper()[0]
    e = 1 if e == 'I' else 0
    print(f'Você jogou {n} e o computador{nc}.Total de {s}', end=' ')
    print(f'DEU PAR' if s%2 == 0 else f'DEU ÍMPAR')
    print('=-='*10)
    if e != s%2:
        break
    else:
        print(f'Você VENCEU!\nVamos jogar novamente...')
        cont += 1
    print('=-='*10)
print(f'Você perdeu!')
print('=-='*10)
print(f'GAME OVER! Você ganhou {cont} vezes')