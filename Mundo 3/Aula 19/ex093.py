jogador = dict()
partidas = list()
jogador ['nome']= str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o {jogador ["nome"]} participou? '))
for c in range(0, tot):
    partidas.append(int(input(f'    Total de gols na partida {c +1}:  ')))
jogador ['gols'] = partidas[:]
jogador ['total'] = sum (partidas)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print()
print(f' o Jogador {jogador["nome"]} participou de {len(jogador["gols"])} partidas. ')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i} fez {v} gols.')
print(f'Foi total de {jogador["total"]} gols!')