def mensagem():
    print('Texto da função')

mensagem()

def mensagem(texto):
    print(texto)

mensagem('Texto com parâmetro')

def soma(a, b):
    print(a + b)

soma(5, 3)

def soma2(a, b):
    return a + b

resultado = soma2(5, 5)

print(resultado)

def calcula_energia_potencial_gravitacional(m, h, g = 10):
    '''
        Calcula a energia potencial gravitacional

        Argumentos:
        m = massa, entrada como float
        h = altura, entrada como float
        
        Opcional:
        g =  aceleração gravitacional, com default 10
    '''
    e = g * m * h
    return e

print(calcula_energia_potencial_gravitacional(30, 12))

help(calcula_energia_potencial_gravitacional)