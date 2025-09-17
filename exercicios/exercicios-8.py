alunos = {}

for i in range(0, 3):
    i += 1
    nome = str(input(f'Qual é o nome do aluno {i}: '))
    nota = float(input(f'Qual é a nota do aluno {i}: '))

    alunos[nome] = nota

print(alunos)

media_notas = 0

for aluno in alunos.values():
    media_notas += aluno

media_notas = media_notas / 3

print('A média de todas as notas dos alunos é:', media_notas)

