print('-=' *15)
print('Analise os triângulos ')
print('-='*15)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima  podem formar triângulo! ')
else:
    print(' Os seguimentos acima não podem formar triângulo! ')