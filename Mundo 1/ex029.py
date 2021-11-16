velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('Multado! Você ultrapassou o límite permitido que é de 80km/h  ')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenhe um bom dia! Dirija com segurança!')