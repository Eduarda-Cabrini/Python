from random import randint
from time import sleep
itens = ('pedra', 'papel','tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] papel
[ 3 ] tesoura ''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-#-'*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-#-'*11)
if computador == 0 : # computador jogou pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Empate')
    else: 
        print('Jogada inválida! ')

elif computador == 1: # computador jogou papel

    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate ')
    elif jogador == 2:
        print('Jogador vence')
    else: 
        print('Jogada inválida! ')

elif computador == 2: #computador jogou tesoura

    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else: 
        print('Jogada inválida! ')