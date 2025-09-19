# NameError: variável nao foi definida
# TypeError: tipos de dados incompatíveis
# RuntimeError: erro de execução
# SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
# ZeroDivisionError: divisão por zero
# IndexError: índice está fora da coleção

# 3 = 4 SyntaxError

# print('Meu nome é', nome) NameError

# print(3 / 0) ZeroDivisionError

# 2.3 / 'cachorro' TypeError

c = [1, 2, 3, 4, 5]

# print(c[5]) IndexError

while True:
    try:
        n = int(input('Digite um número inteiro: ')) # ValueError
    except:
        print('Valor inválido!')
    else:
        print(f'Valor digitado é {n}')
        break

while True:
    try:
        p = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Valor inválido!')
    except KeyboardInterrupt:
        print('Usuário interrompeu a execução!')
    else:
        print(f'Valor digitado é {p}')
        break