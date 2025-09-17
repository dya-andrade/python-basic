numeros = []

for i in range(0, 5):
    i += 1
    numero = int(input(f'Informe o número {i}: '))
    numeros.append(numero)

print(numeros)

soma = 0

for numero in numeros:
    soma += numero

print('A soma total dos números digitados:', soma)