from datetime import date
atual = date.today().year
totmaior = 0
totmenos = 0 
for pess in range(1, 8):
    nac = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nac
    if idade >= 21:
        totmaior += 1 
    else: 
        totmenos += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenos))
    


    
