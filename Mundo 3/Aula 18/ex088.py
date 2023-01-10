from random import randint
from time import sleep
lista = list()
sorteado = list()
print(f'{"Sortedos na Mega-Sena":=^60}')
while True :
    sorteado.clear()
    jogo = int(input("Quantos jogos deseja ver : "))
    limit = 0
    while jogo > limit :    
        cont = 0
        while True :
            num = randint(1,60)
            if num not in lista :
                lista.append(num)
            cont += 1
            if cont >= 6 :
                lista.sort()
                sorteado.append(lista[:])
                lista.clear()
                break
        limit += 1
    print(f'Gerando {jogo} jogos...')
    sleep(1)
    for indice ,p in enumerate(sorteado):
        print(f'jogo {indice + 1} : {p}')
        sleep(1)
    print('Boa sorte!')
    print('='*30)
