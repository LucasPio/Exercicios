vogais = ('a', 'e', 'i', 'o', 'u')
palavras = ('Viagem', 'morar', 'namorar', 'viver', 'entender', 'aprender')
for palavra in palavras:
    print(f'\nvogais da palavra {palavra} ',end='' )
    for letra in palavra:
        if letra.lower() in vogais:

            print(letra, end=' ')