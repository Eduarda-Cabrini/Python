frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.strip()
junto = ''.join(palavras)
inv = ''
for letra in range(len(junto) -1, -1, -1):
    inv += junto [letra]
print('o inverso de {} é {}'.format(junto, inv))
if inv == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo !')