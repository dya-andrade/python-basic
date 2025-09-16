print('Cálculo da quantidade de litros de combustível gasto em uma viagem: ')

tempo = float(input('Tempo gasto: '))
velocidade_media = float(input('Velocidade média: '))

distancia = tempo * velocidade_media
print('Distância percorrida:', distancia)

litro_por_km = 12
litros_usados = distancia / litro_por_km

print('Quantidade de litros usados:', round(litros_usados, 1))