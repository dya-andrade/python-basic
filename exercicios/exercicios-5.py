contador = 1
media_notas = 0

while contador < 6:
    nota = float(input(f'Informe a nota {contador}: '))
    media_notas += nota
    contador += 1

media_notas = media_notas/5

print('A média das 5 notas é:', media_notas)