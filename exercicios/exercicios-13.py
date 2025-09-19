alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('alunos.txt', 'w') as txt:
    for aluno, nota in alunos.items():
        txt.write(f'{aluno}, {nota}\n')

with open('alunos.txt') as txt:
    for linha in txt:
        print(linha)