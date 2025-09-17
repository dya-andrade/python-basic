for numero in range(1, 6):
    print(numero)

print()

for numero in range(6, 0, -1):
    print(numero)

print()

soma = 0
for numero in range(1, 6):
    soma = soma + numero
    print(soma)

print(soma)

print()

palavra = 'sorvete'

for letra in palavra:
    print(letra)
    if letra == 'o':
        print('Achou a letra o')

print()

for i in range(0, 5):
    print(i)
    print('----')
    for j in range(0, 3):
        print(j)
    print()

print()

numero = 1

while numero < 6:
    print(numero)
    numero += 1

print()

numero = 5

while numero > 0:
    print(numero)
    numero -= 1

print()

soma = 0
numero = 1

while numero < 6:
    soma = soma + numero
    numero += 1
print(soma)

print()

numero = -1

while numero < 1 or numero > 10:
    numero = int(input('Digite um número de 1 a 10: '))