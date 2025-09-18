# https://docs.python.org/3/library/math.html
import math

math.sqrt(9) # raiz quadrada
math.sin(45) # seno
math.cos(45) # conseno
math.log(1000, 10) # logaritmo e base
math.log(1000) # logaritmo sem base
math.e # número Euler
math.pi # número PI

# https://docs.python.org/3/library/datetime.html
import datetime

dir(datetime) # verificar os recursos que existem

datetime.datetime.today()
datetime.datetime.now()

data = datetime.date(2020, 7, 10)
data.day
data.month
data.year

horario = datetime.datetime(2020, 7, 10, 7, 30,0)
horario.hour
horario.minute
horario.second

# https://docs.python.org/3/library/random.html
import random

random.random()

random.randint(1, 10) # gera números random entre 1 a 10
random.randrange(0, 10, 2) # gera números pares
random.randrange(0, 10, 3) # gera números múltiplos de 3

x = ['k', 'd', 13, '34-j', 'x']

random.choice(x) # sortea

# https://docs.python.org/3/library/time.html
import time as tm

tm.time() # tempo atual em segundos

antes = tm.time()

lista = []

for i in range(0, 10000):
    lista.append(i)

depois = tm.time()

intervalo = depois - antes

print(f'Tempo: {intervalo} segundos.')

print('Finalizando...')
tm.sleep(2) # em segundos

print('...')

tm.sleep(2)
print('Até a próxima!')