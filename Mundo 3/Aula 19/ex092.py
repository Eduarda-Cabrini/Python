from datetime import datetime
dados = dict()
dados ['nome'] = str(input('nome: '))
nasc = int(input('Ano de nascimento: '))
dados ['idade'] = datetime.now().year - nasc
dados ['ctps'] = int(input('Carteira de trabalho: (0 se não ter: )'))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('___'* 25)
for k, v in dados.items():
    print(f'  {k} : {v}')