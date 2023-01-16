boletim = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1º nota: '))
    nota2 = float(input('2º nota: '))
    media = (nota1 + nota2 ) / 2
    boletim.append( [nome, [nota1, nota2], media])
    aluno = str(input('Quer adicionar outro aluno? [S/N]'))
    if aluno in 'Nn': 
        break
print('='*50)
print(f'{"Num.":>4}{"Nome":<10}{"Média":>8}')
print('--'*30)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('=' * 30)
    opc = int(input('Mostrar notas de qual aluno? (000 interrompe):'))
    if opc == 0:
        print('Finalizando...')
        break
    if opc <= len(boletim) - 1:
        print(f'Notas do {boletim [opc] [0]} são {boletim [opc] [1]}')