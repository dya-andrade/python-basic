numero = int(input('Digite o número: '))
print(f'Tabuada do {numero}:')

for i in range (0, 10):
    i += 1
    print(f'{numero} x {i} =', numero * i)
    # print('{} x {} = {}'.format(numero, i, numero * i))

