while True:
    try:
        tamanho = int(input('Informa o tamanho da lista: '))
    except ValueError:
        print('Valor tem que ser um float!')
    else:
        break

lista = []

for i in range(0, tamanho):
    while True:
        try:
            numero = float(input(f'Digite o valor {i}: '))
        except ValueError:
            print('Valor tem que ser um float!')
        except KeyboardInterrupt:
            print('Usuário interropeu o programa!')
        else:
            lista.append(numero)
            break

for i in range(0, tamanho):
    try:
        divisão = lista[i] / lista[i + 1]
    except ZeroDivisionError:
        print('Não é possível fazer divisão por zero.')
    except KeyboardInterrupt:
        print('Usuário interropeu o programa!')
    except IndexError:
        break
    else:
        print('O resultado da divisão:', divisão)

