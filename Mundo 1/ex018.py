import math
ângulo = float(input('Digite o ângulo que você deseja: '))
Seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ângulo, Seno))
cos = math.cos(math.radians(ângulo))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ângulo, cos))
Tan = math.tan(math.radians(ângulo))
print('o ângulo de {} tem a Tangente de {:.2f}'.format(ângulo, Tan))