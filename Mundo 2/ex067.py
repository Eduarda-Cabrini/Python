while True:
    num = int(input('Qual número de tabuada você gostaria de ver? '))
    if num < 0:
        break
    print('-' * 50)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' * 50 )
print('Tabuada encerrada...')