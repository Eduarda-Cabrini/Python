soma = cont = 0
while True:
    num = int(input('Digite um valor (use 000 para encerrar): '))
    if num == 000:
            break
    soma += num
    cont += 1
print('A soma dos {} valores foi para {}' .format(cont, soma))