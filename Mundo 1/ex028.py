from random import randint
computador = randint(0, 5)
print('-*-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-*-' * 20)
jogador = int(input('Em que número eu pensei?'))
if  jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else :
    print('Ganhei! eu pensei no número {} e não no numero {}!'.format(computador, jogador))