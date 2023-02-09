time = list()
jogador = dict()
partidas = list()

while True:
    jogador ['nome']= str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador ["nome"]} participou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Total de gols na partida {c +1}:  ')))
    jogador ['gols '] = partidas[:]
    jogador ['total '] = sum (partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('erro! Responda apenas com s/N')
    if resp == 'N':
        break

print('cod', end='')   
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
for k, v in enumerate (time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()      
print()
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! não existe jogador com código {busca} na lista ')
    else:
        print(f'-----Sobre o jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' No jogo {i} fez {g} gols.')
print('Volte sempre S2')