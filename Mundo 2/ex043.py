from typing import ItemsView


peso = float(input('Qual é seu peso? (kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}' .format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif 18.5 <= imc < 25 :
    print('Você está na faixa de peso normal')        
elif 25 <= imc < 30 :
    print('Você está sobrepeso normal ')
elif 30 <= imc < 40 :
    print('Você está com obesidade ') 
elif imc >= 40 :
    print('Você está com obesidade mórbida')
