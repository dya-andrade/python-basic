with open('frase1.txt') as tex:
    read = tex.readlines()
    print(read)

    for linha in read:
        print(linha)

with open('texto2.txt', 'w') as texto:
    texto.write('Olá a todos!')