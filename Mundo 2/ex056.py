somaidade = 0
mediaidade = 0
marioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-/-/-/-/- {}ª -/-/-/-/-'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade =+ idade 
    if p == 1 and sexo in 'Mm':
        marioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > marioridadehomem:
        marioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade de grupo é de {} anos '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(marioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))