galera = list()
pessoa = dict()
soma = média = 0 
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [F/M]')).upper()[0]
        if pessoa ['sexo'] in 'MF':
            break
        print('Erro! Por favor digite novamente[M/F]')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Por favor, responda com [S/N]')
    if resp == 'N':
        break
print(f'Ao todo temod {len(galera)} pessoas cadastradas. ')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos')
print(f'As mulheres cadastradas foram',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ',end='')
print()
print(f'Lista das pessoas que estão acima da média ', end='')
for p in galera:
    if p['idade'] >= média:
        print('        ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()     