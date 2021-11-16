
from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
else:
    print('O ano {} não é bissexto'.format(ano))
if ano % 4 == 0 and ano % 100 != 0 or ano % 4 == 0:
    print('O ano {} é bissexto'.format(ano))