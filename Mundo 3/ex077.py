palavras = ('Aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aáãâeéêiíoôõóu' :
            print(letra, end='')